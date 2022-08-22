from datetime import datetime
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Text, DATETIME
from sqlalchemy.orm import relationship

from core.db import Base
from utils.depends import makeslug


articles_themes_table = Table(
    "association",
    Base.metadata,
    Column("article_id", ForeignKey("article.id")),
    Column("theme_id", ForeignKey("theme.id"))
)


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, unique=True)
    subtitle = Column(String)
    maintext = Column(Text)
    created = Column(DATETIME, default=datetime.now())

    associated_themes = relationship("AssociatedThemes", secondary=articles_themes_table)


class AssociatedThemes(Base):
    __tablename__ = "theme"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    slug = Column(String, unique=True)

    def __init__(self, *args, **kwargs):
        super(AssociatedThemes, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = makeslug(self.name)

    def __repr__(self):
        return self.name
