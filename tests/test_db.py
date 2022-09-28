from datetime import datetime
from faker import Faker
# from fastapi.testclient import TestClient
from core.db import *
# from main import app, db_session_middleware
from user.models import User
from .client import client


def generate_fake_userdata():
    fake = Faker()
    uname = fake.name()
    mail = fake.email()
    pswd = fake.password()
    return uname, mail, pswd


# SQLALCHEMY_DATABASE_URL = "postgresql://dima:12345@localhost/test_db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base.metadata.create_all(bind=engine)
#
#
# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()
#
#
# app.dependency_overrides[db_session_middleware] = override_get_db
name, email, password = generate_fake_userdata()


def test_create_user():
    response = client.post(
        "user/create", json={"name": name, "email": email, "password": password,
                             "date": str(datetime.now())}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "access_token" in data
    session.query(User).filter(User.name == name).delete(synchronize_session=False)
    session.commit()


def test_get_current_user():
    users = session.query(User).all()
    user_id = 1
    response = client.get(f"user/{user_id}")
    if user_id <= len(users):
        assert response.status_code == 200
        data = response.json()
        assert "user_info" in data
        assert "user_articles" in data


def test_get_current_user_error():
    users = session.query(User).all()
    user_id = 1234124
    response = client.get(f"user/{user_id}")
    if user_id <= len(users):
        assert response.status_code == 200
        data = response.json()
        assert data == {"message": "User with current id does not exists!"}
