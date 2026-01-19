from app.main import app


def test_home_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_response_content():
    client = app.test_client()
    response = client.get("/")
    assert response.json == {"message": "API DevSecOps OK"}
