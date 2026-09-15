from fastapi.testclient import TestClient


def test_create_character_api(client: TestClient) -> None:
    actor = client.post(
        "/actors/",
        json={
            "first_name": "Dan",
            "last_name": "Castellaneta",
            "cast": "Main",
        },
    ).json()

    payload = {
        "name": "Homer Simpson",
        "actor_id": actor["id"],
    }

    res = client.post("/characters/", json=payload)
    assert res.status_code == 201

    data = res.json()
    assert data["name"] == "Homer Simpson"
    assert data["id"] is not None


def test_get_character_api(client: TestClient) -> None:
    actor = client.post(
        "/actors/",
        json={
            "first_name": "Dan",
            "last_name": "Castellaneta",
            "cast": "Main",
        },
    ).json()

    create = client.post(
        "/characters/",
        json={
            "name": "Homer Simpson",
            "actor_id": actor["id"],
        },
    ).json()

    res = client.get(f"/characters/{create['id']}")
    assert res.status_code == 200
    assert res.json()["name"] == "Homer Simpson"


def test_update_character_api(client: TestClient) -> None:
    actor = client.post(
        "/actors/",
        json={
            "first_name": "Dan",
            "last_name": "Castellaneta",
            "cast": "Main",
        },
    ).json()

    create = client.post(
        "/characters/",
        json={
            "name": "Homer Simpson",
            "actor_id": actor["id"],
        },
    ).json()

    res = client.put(
        f"/characters/{create['id']}",
        json={
            "name": "Krusty the Clown",
            "actor_id": actor["id"],
        },
    )

    assert res.status_code == 200
    assert res.json()["name"] == "Krusty the Clown"


def test_delete_character_api(client: TestClient) -> None:
    actor = client.post(
        "/actors/",
        json={
            "first_name": "Dan",
            "last_name": "Castellaneta",
            "cast": "Main",
        },
    ).json()

    character = client.post(
        "/characters/",
        json={
            "name": "Homer Simpson",
            "actor_id": actor["id"],
        },
    ).json()

    res = client.delete(f"/characters/{character['id']}")
    assert res.status_code == 204

    res = client.get(f"/characters/{character['id']}")
    assert res.status_code == 404
