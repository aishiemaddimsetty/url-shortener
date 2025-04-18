A FastAPI-based backend to shorten and retrieve URLs (like Bitly).

Features
Create short URLs
Retrieve original URLs using short codes
Built using FastAPI, SQLAlchemy, and SQLite
Requirements
pip install -r requirements.txt

---

## Run the Server

Start the FastAPI development server using:

```bash
uvicorn app.main:app --reload

---

Once the server is running, you can use these endpoints:

POST /shorten

Send a JSON body to shorten a URL:

{
  "original_url": "https://github.com"
}

---

GET /original/{short_code}

Use the short code to retrieve the original URL:

```bash
/original/abc123

---

Example 
1. POST to /shorten with:

```json

{
  "original_url": "https://github.com"
}
Response:

```json
{
  "original_url": "https://github.com",
  "short_code": "abc123"
}

2. GET /original/abc123

Response:

```json

{
  "original_url": "https://github.com"
}
