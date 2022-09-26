from sqlalchemy.orm import Session
from topforum.models import Article
from .schema import ArticleCreate


# Что бы не забыть
#
# session.query(MODEL).all()
# session.query(MODEL).first()
# и т. д.



def get_articles_list(db: Session):
    return db.query(Article).all()


def create_article(db: Session, item: ArticleCreate):
    article = Article(**item.dict())
    db.add(article)
    db.commit()
    db.refresh(article)
    return article
