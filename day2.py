from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "user": user
    }

user=User(name="Alice", age=30)
create_user(user)