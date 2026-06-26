from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


# Strict type checking for user_id path parameter, string will be rejected
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}


# Tidyer query parameters, we don't need to put these in the path decorator.
@app.get("/users/")
def get_users(page: int = 1):
    fake_users = [f"User {i}" for i in range((page - 1) * 10 + 1, page * 10 + 1)]
    return {
        "page": page,
        "users": fake_users,
    }


# Automatic post validation using pydantic
@app.post("users/")
def create_user(user: User):
    return f"User {user.name} created!"
