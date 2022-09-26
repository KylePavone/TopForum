from fastapi import APIRouter
from topforum import topforum
from user import user


routes = APIRouter()


routes.include_router(topforum.router, prefix="/articles")
routes.include_router(user.user_router, prefix="/user")
