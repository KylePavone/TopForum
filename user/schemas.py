from datetime import datetime, timezone
from typing import List
from pydantic import BaseModel, Field, EmailStr
from topforum.schema import ArticleBaseSchema


class UserSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    date: datetime
    articles: List[ArticleBaseSchema] = []
    is_active: bool = Field(default=False)
    is_admin: bool = Field(default=False)

    class Config:
        schema_extra = {
            "example": {
                "name": "KylePavone",
                "email": "kyle2000@gmail.com",
                "password": "weakpassword",
                "date": datetime(2022, 9, 26, 21, 29, 33, 150000, tzinfo=timezone.utc),
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "Your email",
                "password": "Your password"
            }
        }
