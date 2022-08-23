from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.depends import get_db
from . import service
from .schema import ArticleCreate, ArticleList

router = APIRouter()


@router.get("/all", response_model=List[ArticleList])
async def articles_list(db: Session = Depends(get_db)):
    return service.get_articles_list(db)


@router.post("/all")
async def articles_list(item: ArticleCreate, db: Session = Depends(get_db)):
    return service.create_article(db, item)
