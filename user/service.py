from sqlalchemy.orm import Session
from .schemas import UserSchema, UserLoginSchema
from core.db import *
from .models import User


def create_user(db: Session, item: UserSchema):
    user = User(**item.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def check_user(data: UserLoginSchema):
    users = session.query(User).all()
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False
