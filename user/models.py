from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base
from . import security

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String)
    date = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    articles = relationship("Article")


    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.password = self.hash_password()

    def __repr__(self):
        return f"User {self.name} -- {self.email}"

    def hash_password(self):
        return security.get_password_hash(self.password)








