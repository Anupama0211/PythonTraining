import requests_mock


def test_library_get_book_by_id(client):
    with requests_mock.Mocker() as rm:
        rm.get('http://127.0.0.1:5001/books/1', json={"name": "Book"},
               status_code=200)
        response = client.get("library/books/1")
        assert response.status_code == 200
        assert response.json == {"name": "Book"}


def test_library_get_books_list(client):
    with requests_mock.Mocker() as rm:
        rm.get('http://127.0.0.1:5001/books', json=[{"name": "Book"}],
               status_code=200)
        response = client.get("library/books")
        assert response.status_code == 200
        assert response.json == [{"name": "Book"}]


def test_library_post_book(client):
    with requests_mock.Mocker() as rm:
        rm.post('http://127.0.0.1:5001/books', json={"name": "Book"},
                status_code=201)
        response = client.post("library/books", json={"name": "Book"})
        assert response.status_code == 201
        assert response.json == {"name": "Book"}
