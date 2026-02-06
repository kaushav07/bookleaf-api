# BookLeaf Author Earnings API

A backend API to manage authors, book sales, earnings, and withdrawals for BookLeaf Publishing.

## Tech Stack

- Python with FastAPI
- In-memory data storage using Python data structures

FastAPI was chosen for its simplicity, built-in validation, and clean API design.  
In-memory storage was used as allowed by the assignment to keep the project lightweight.

## Features

- Fetch all authors with total earnings and current balance
- Fetch detailed author information with books and royalties
- View sales history for an author
- Create withdrawal requests with validation
- Proper HTTP status codes and error handling

## API Endpoints

- GET /authors  
- GET /authors/{id}  
- GET /authors/{id}/sales  
- POST /withdrawals  
- GET /authors/{id}/withdrawals  

## Assumptions

- Earnings are calculated dynamically from sales data.
- Withdrawals reduce the current balance but do not change total earnings.
- Data resets on server restart as in-memory storage is used.
- Sale dates are handled as strings and sorted accordingly.

## Validation Rules

- Minimum withdrawal amount is ₹500
- Withdrawal amount cannot exceed current balance
- Author must exist
- Correct HTTP status codes are returned

## Running Locally

pip install -r requirements.txt  
python app.py  

The server runs at:
http://127.0.0.1:8000

## Deployed URL

https://bookleaf-api-x8ts.onrender.com

Example test:
GET /authors

## Time Spent

Approximately 5–6 hours including development, testing, deployment, and documentation.

## Notes

The focus of this project was clean, readable, and maintainable code, as requested in the assignment.
