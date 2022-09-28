from datetime import datetime
from faker import Faker
from core.db import *
from user.models import User
from .client import client


def generate_fake_userdata():
    fake = Faker()
    uname = fake.name()
    mail = fake.email()
    pswd = fake.password()
    return uname, mail, pswd


def create_user_request():
    user = session.query(User).filter(User.name == "KylePavone").first()
    try:
        response = client.post(
            "user/create", json={"name": user.name, "email": user.email, "password": password,
                                 "date": str(datetime.now())}
        )
        return response
    except:
        return None


name, email, password = generate_fake_userdata()


def test_create_user_success():
    response = client.post(
        "user/create", json={"name": name, "email": email, "password": password,
                             "date": str(datetime.now())}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "access_token" in data
    session.query(User).filter(User.name == name).delete(synchronize_session=False)
    session.commit()


def test_create_user_error():
    assert create_user_request() is None


def test_get_current_user_success():
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
    user_id = len(users) + 1
    response = client.get(f"user/{user_id}")
    if user_id <= len(users):
        assert response.status_code == 200
        data = response.json()
        assert data == {"message": "User with current id does not exists!"}
