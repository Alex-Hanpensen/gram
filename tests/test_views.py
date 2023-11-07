from app import app


def test_app():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert response.json[0].get('poster_name') is not None


def test_app_2():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    assert isinstance(response.json[0], dict)
    assert response.json[0].get('poster_name') is not None
