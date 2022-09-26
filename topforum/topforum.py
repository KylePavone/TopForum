from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.depends import get_db
from . import service
from .schema import ArticleCreate, ArticleList, ArticleBaseSchema
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT


router = APIRouter()


@router.get("/all", response_model=List[ArticleList])
async def articles_list(db: Session = Depends(get_db)):
    return service.get_articles_list(db)


@router.post("/create", dependencies=[Depends(JWTBearer())])
async def create_article(item: ArticleCreate, db: Session = Depends(get_db)):
    return service.create_article(db, item)
