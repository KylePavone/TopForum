import json
from fastapi import FastAPI
from topforum_models.models import Article, AssociatedThemes
from core.db import session


app = FastAPI()


@app.get("/all")
async def all_titles():
    first_theme = session.query(Article).first()
    return first_theme
