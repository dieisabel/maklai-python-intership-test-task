def test_paraphrase_endpoint(client):
    expected = {"hello": "world!"}
    response = client.get("/paraphrase")
    assert response.json == expected
