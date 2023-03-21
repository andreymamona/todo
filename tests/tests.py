import requests


if __name__ == "__main__":
    response = requests.get("http://127.0.0.1:8000")
    assert response.status_code == 200
    assert 'Add Notes' in str(response.content)

    response = requests.get("http://127.0.0.1:8000/admin/")
    assert response.status_code == 200
