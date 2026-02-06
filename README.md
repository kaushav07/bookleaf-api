# BookLeaf Author Royalties API

This project is a backend REST API built for BookLeaf Publishing.  
It handles author data, book sales, royalty calculations, and withdrawal requests based on the rules provided in the assignment PDF.

---

## Tech Stack

- **Backend:** Python (FastAPI)
- **Database:** In-memory data storage (Python data structures)
- **Deployment:** Render (Free tier)
- **UI (optional):** Single-page HTML deployed on Vercel

FastAPI was chosen for its simplicity, clean routing, and built-in request validation.  
In-memory storage was used as explicitly allowed in the assignment to keep the focus on business logic rather than database setup.

---

## Features Implemented

- Fetch all authors with calculated total earnings and current balance
- Fetch detailed author information including books and royalty breakdown
- View all sales for an author, sorted by date (newest first)
- Create withdrawal requests with all required validations
- View withdrawal history for an author
- Proper HTTP status codes and clear error messages

---

## API Endpoints

```text
GET    /authors
GET    /authors/{id}
GET    /authors/{id}
GET    /authors/{id}/sales
POST   /withdrawals
GET    /authors/{id}/withdrawals
````

---

## Business Rules & Assumptions

* Total earnings are calculated dynamically from sales data
* Current balance = total earnings minus withdrawals
* Withdrawals do not modify total earnings
* Data resets on server restart since in-memory storage is used
* Sale dates are handled as strings and sorted accordingly

---

## Validation Rules

* Minimum withdrawal amount is ₹500
* Withdrawal amount cannot exceed current balance
* Author must exist
* Correct HTTP status codes are returned:

  * `400` for validation errors
  * `404` when author is not found
  * `201` when a withdrawal is successfully created

---

## Running the Project Locally

```bash
pip install -r requirements.txt
python app.py
```

The server will start at:

```text
http://127.0.0.1:8000
```

Test example:

```text
GET /authors
```

---

## Deployed API (Render)

The API is deployed on Render as required.

```text
https://bookleaf-api-x8ts.onrender.com
```

You can verify deployment by opening:

```text
https://bookleaf-api-x8ts.onrender.com/authors
```

---

## Optional Testing UI (Vercel)

A simple, modern single-page UI was created to make manual testing easier without Postman.

* Displays authors, sales, balances, and withdrawals in a readable format
* Allows creating withdrawals directly from the browser
* Uses the same deployed API (no backend changes)

UI Link:

```text
https://bookleaf-ui.vercel.app
```

This UI is optional and provided only to simplify testing and demonstration.
The backend API fully satisfies the assignment requirements on its own.

---

## Time Spent

Approximately **3 hours**, including:

* API development
* Manual testing (Postman + browser)
* Deployment on Render
* Documentation
* Optional UI for easier evaluation

---

## Final Note

The goal of this assignment was to write clean, readable, and maintainable code that follows the provided requirements closely.
The implementation focuses on correctness and clarity rather than unnecessary complexity.

---
