import json
import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()
    # clean up / reset resources here


def test_ping(client):
    # Given
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    expected = {"status": "success", "detail": "pong!"}

    # When
    response = client.get('/ping', headers=headers)

    # Then
    assert response.status_code == 200
    json_dict = json.loads(response.data)
    assert json_dict == expected


def test_post(client):
    # Given
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    post_data = {"postdump": "mydata"}
    expected = {"postdump": "mydata"}

    # When
    response = client.post('/post', 
                           data=json.dumps(post_data), 
                           headers=headers)
    
    # Then
    assert response.status_code == 200
    json_dict = json.loads(response.data)
    assert json_dict == expected

