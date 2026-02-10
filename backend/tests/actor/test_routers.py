from fastapi.testclient import TestClient


def test_create_actor_api(client: TestClient) -> None:
    payload: dict[str, str] = {
        "first_name": "Dan",
        "last_name": "Castellaneta",
        "cast": "Homer",
    }

    res = client.post("/actors/", json=payload)
    assert res.status_code == 200

    data: dict[str, object] = res.json()
    assert data["first_name"] == "Dan"
    assert data["id"] is not None


def test_get_actor_api(client: TestClient) -> None:
    payload: dict[str, str] = {
        "first_name": "Julie",
        "last_name": "Kavner",
        "cast": "Marge",
    }
    create: dict[str, object] = client.post("/actors/", json=payload).json()

    res = client.get(f"/actors/{create['id']}")
    assert res.status_code == 200
    assert res.json()["last_name"] == "Kavner"


def test_update_actor_api(client: TestClient) -> None:
    create: dict[str, object] = client.post(
        "/actors/",
        json={
            "first_name": "Nancy",
            "last_name": "Cartwright",
            "cast": "Bart",
        },
    ).json()

    res = client.put(
        f"/actors/{create['id']}",
        json={
            "first_name": "Nancy",
            "last_name": "Cartwright",
            "cast": "Bart Simpson",
        },
    )

    assert res.status_code == 200
    assert res.json()["cast"] == "Bart Simpson"


def test_delete_actor_api(client: TestClient) -> None:
    create = client.post(
        "/actors/",
        json={
            "first_name": "Hank",
            "last_name": "Azaria",
            "cast": "Moe",
        },
    ).json()

    res = client.delete(f"/actors/{create['id']}")
    assert res.status_code == 204

    res = client.get(f"/actors/{create['id']}")
    assert res.status_code == 404
