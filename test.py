from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI by jayam 🚀"}

@app.get("/items")
def get_items():
    return ["Pen", "Book", "Laptop"]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/search")
def search(keyword: str, page: int = 1):
    return {"keyword": keyword, "page": page}


from fastapi import Query

@app.get("/items/search")
def read_items(
    q: str = Query(min_length=3, max_length=10),
    limit: int = Query(gt=0, le=100)
):
    return {"q": q, "limit": limit}
