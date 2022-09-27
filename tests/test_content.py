from .client import client


def test_get_all_articles():
    response = client.get("articles/all")
    assert response.status_code == 200
