from datetime import datetime
from pydantic import BaseModel


class ArticleBaseSchema(BaseModel):
    title: str
    subtitle: str
    maintext: str
    created: datetime
    user_id: int

    class Config:
        orm_mode = True


class ArticleList(ArticleBaseSchema):
    id: int


class ArticleCreate(ArticleBaseSchema):
    pass
