from sqlalchemy import Table, Column, ForeignKey, Integer, String, Text, DateTime
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
    title = Column(String(255), unique=True)
    slug = Column(String(255), unique=True)
    subtitle = Column(String(255))
    maintext = Column(Text)
    created = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship("User")
    associated_themes = relationship("AssociatedThemes", secondary=articles_themes_table)

    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = makeslug(self.title)

    def __repr__(self):
        return f"Article --- {self.title}"


class AssociatedThemes(Base):
    __tablename__ = "theme"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255))
    slug = Column(String(255), unique=True)

    def __init__(self, *args, **kwargs):
        super(AssociatedThemes, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = makeslug(self.name)

    def __str(self):
        return self.name

    def __repr__(self):
        return f"Theme --- {self.name}"
