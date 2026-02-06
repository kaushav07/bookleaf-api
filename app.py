from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from data import authors, books, sales, withdrawals
from models import WithdrawalRequest

app = FastAPI()

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#HELPER FUNCTIONS
def calculate_total_earnings(author_id: int):
    total = 0
    for sale in sales:
        book = books[sale["book_id"]]
        if book["author_id"] == author_id:
            total += sale["quantity"] * book["royalty"]
    return total


def calculate_current_balance(author_id: int):
    total_earnings = calculate_total_earnings(author_id)
    withdrawn = sum(
        w["amount"] for w in withdrawals if w["author_id"] == author_id
    )
    return total_earnings - withdrawn


#ENDPOINTS
@app.get("/authors")
def get_authors():
    result = []
    for author in authors.values():
        result.append({
            "id": author["id"],
            "name": author["name"],
            "total_earnings": calculate_total_earnings(author["id"]),
            "current_balance": calculate_current_balance(author["id"]),
        })
    return result


@app.get("/authors/{author_id}")
def get_author(author_id: int):
    if author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")

    author = authors[author_id]

    author_books = []
    for book in books.values():
        if book["author_id"] == author_id:
            total_sold = sum(
                s["quantity"] for s in sales if s["book_id"] == book["id"]
            )
            author_books.append({
                "id": book["id"],
                "title": book["title"],
                "royalty_per_sale": book["royalty"],
                "total_sold": total_sold,
                "total_royalty": total_sold * book["royalty"],
            })

    return {
        "id": author["id"],
        "name": author["name"],
        "email": author["email"],
        "total_earnings": calculate_total_earnings(author_id),
        "current_balance": calculate_current_balance(author_id),
        "total_books": len(author_books),
        "books": author_books,
    }


@app.get("/authors/{author_id}/sales")
def get_author_sales(author_id: int):
    if author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")

    result = []
    for sale in sales:
        book = books[sale["book_id"]]
        if book["author_id"] == author_id:
            result.append({
                "book_title": book["title"],
                "quantity": sale["quantity"],
                "royalty_earned": sale["quantity"] * book["royalty"],
                "sale_date": sale["date"],
            })

    result.sort(key=lambda x: x["sale_date"], reverse=True)
    return result


@app.post("/withdrawals", status_code=201)
def create_withdrawal(request: WithdrawalRequest):
    if request.author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")

    if request.amount < 500:
        raise HTTPException(status_code=400, detail="Minimum withdrawal is ₹500")

    current_balance = calculate_current_balance(request.author_id)
    if request.amount > current_balance:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    withdrawal = {
        "id": len(withdrawals) + 1,
        "author_id": request.author_id,
        "amount": request.amount,
        "status": "pending",
        "created_at": datetime.utcnow().isoformat(),
    }

    withdrawals.append(withdrawal)
    withdrawal["new_balance"] = calculate_current_balance(request.author_id)

    return withdrawal


@app.get("/authors/{author_id}/withdrawals")
def get_withdrawals(author_id: int):
    if author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")

    result = [
        w for w in withdrawals if w["author_id"] == author_id
    ]
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return result
