from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from .schemas import UserSchema, UserLoginSchema
from . import service
from utils.depends import get_db
from auth import auth_handler


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
        "error": "Wrong login details!"
    }
