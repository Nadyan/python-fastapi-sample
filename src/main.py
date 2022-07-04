from fastapi import FastAPI, HTTPException
from uuid import UUID

from db import db
from models import User

app = FastAPI()


# Routes:

@app.get("/")
def root():
    return {
        "message": "This is a Sample API built using fastAPI framework",
        "GitHub": "github.com/Nadyan"
    }

@app.get("/users")
async def get_users():
    return db

@app.post("/users")
async def insert_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f"user {user_id} not found"
    )

@app.put("/users/{user_id}")
async def update_user(user_update: User, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code = 404,
        detail = f"user {user_id} not found"
    )


"""
    Usage:
        
        - Start the server:
            uvicorn main:app --reload

        - Documentation:
            localhost:8000/docs
            Interactive docs generated automatically by Swagger

            localhost:8000/redoc
            Non interactive docs generated automaticaly
"""
