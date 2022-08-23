from fastapi import APIRouter
from topforum import topforum


routes = APIRouter()

routes.include_router(topforum.router, prefix="/articles")
