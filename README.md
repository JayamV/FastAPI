# FastAPI
My FastAPI learning journey


⚡ FastAPI Learning — Day 1 & Day 2

A structured walkthrough of FastAPI fundamentals, focusing on async concepts, request handling, and parameter validation.

📅 Day 1 — FastAPI Foundations
Topics

What is FastAPI

ASGI vs WSGI

Blocking vs Non-Blocking I/O

FastAPI architecture

Automatic API documentation

Installation
pip install fastapi uvicorn

First Application
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


Run server:

uvicorn main:app --reload

API Documentation

Swagger UI: /docs

ReDoc: /redoc

Key Concepts

Async-first framework

Type-based request validation

Built on ASGI for high concurrency

Validation happens before execution

Day 1 Tasks

/ → Welcome message

/ping → Health check

/square?num=5 → Returns square of number

📅 Day 2 — Path & Query Parameters
Topics

Path parameters

Query parameters

Required vs optional params

Parameter validation

Default values

Path Parameters
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


Always required

Used to identify resources

Type validated automatically

Query Parameters
@app.get("/search")
def search(q: str, page: int = 1):
    return {"query": q, "page": page}


Optional by default

Used for filtering & pagination

Validation with Query
from fastapi import Query

@app.get("/items")
def read_items(
    q: str = Query(min_length=3),
    limit: int = Query(gt=0, le=100)
):
    return {"q": q, "limit": limit}

Path vs Query
Path Parameter	Query Parameter
Identifies resource	Filters/modifies response
Required	Optional
Part of URL path	After ?
Day 2 Tasks

/users/{id}

/search?query=

/products?category=&price=

Add validation constraints