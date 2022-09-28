from .client import client
from core.db import *
from topforum.models import Article


def test_get_all_articles():
    all_articles = session.query(Article).all()
    response = client.get("articles/all")
    assert response.status_code == 200
    arts = set()
    data = response.json()
    for article in all_articles:
        arts.add(str(article))
    for article in data:
        arts.add(article["title"])
    assert len(arts) == len(all_articles)
