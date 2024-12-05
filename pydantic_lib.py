from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()


data = {
    "email": "john@gmail.com",
    "name": "John",
    "age": "20"

}

class User(BaseModel):
    email: EmailStr
    name: str | None = Field(max_length=10)
    age: int = Field(default=0, ge=0, le=100)

    model_config = ConfigDict(extra='forbid')

users = []

@app.post("/users")
def add_user(user: User):
    users.append(user)
    return {"success": True, "message": "User added"}

@app.get("/users")
def get_users():
    return users

