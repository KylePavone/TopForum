from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from .schemas import UserSchema, UserLoginSchema
from . import service
from utils.depends import get_db
from auth import auth_handler
from .models import User
from core.db import session


user_router = APIRouter()


@user_router.post("/create")
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    service.create_user(db, user)
    return auth_handler.signJWT(user.email)


@user_router.post("/login")
async def user_login(user: UserLoginSchema = Body(...)):
    if service.check_user(user):
        return auth_handler.signJWT(user.email)
    return {
        "error": "Wrong credentials!"
    }

@user_router.get("/{user_id}")
async def get_current_user(user_id):
    user = session.query(User).get(user_id)
    if user:
        return {"user_info": user, "user_articles": user.articles}
    return {"message": "User with current id does not exists!"}
