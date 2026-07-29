def test_create_query(client):
    response = client.post(
        "/query",
        json={
            "cadastral_number": "77:01:0000000:123",
            "latitude": 55.7558,
            "longitude": 37.6173,
        },
    )

    assert response.status_code == 200
    assert "cadastral_number" in response.json()
    assert "result" in response.json()