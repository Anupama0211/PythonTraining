def test_get(client):
    response = client.get("/books")
    print(response.status_code)
    print("--------------------")
    print(response.data)

