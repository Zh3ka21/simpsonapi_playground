from os import name
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from simpsonapi_playground.crud.actor import create_actor
from simpsonapi_playground.crud.character import create_character
from simpsonapi_playground.schemas.actors_schemas import ActorCreate
from simpsonapi_playground.schemas.characters_schemas import CharacterCreate


def test_create_character_api(client: TestClient) -> None:
    payload: dict[str, str | int] = {
        "name": "Homer Simpson",
        "actor_id": 1,
    }

    res = client.post("/characters/", json=payload)
    assert res.status_code == 201

    data: dict[str, object] = res.json()
    assert data["name"] == "Homer Simpson"
    assert data["id"] is not None


def test_get_character_api(client: TestClient) -> None:
    payload: dict[str, str | int] = {
        "name": "Homer Simpson",
        "actor_id": 1,
    }
    create: dict[str, object] = client.post("/characters/", json=payload).json()

    res = client.get(f"/characters/{create['id']}")
    assert res.status_code == 200
    assert res.json()["name"] == "Homer Simpson"


def test_update_character_api(client: TestClient) -> None:
    _ = client.post(
        "/actors/",
        json={
            "first_name": "Dan",
            "last_name": "Castellaneta",
            "cast": "Main",
        },
    ).json()

    create: dict[str, object] = client.post(
        "/characters/",
        json={
            "name": "Homer Simpson",
            "actor_id": 1,
        },
    ).json()

    res = client.put(
        f"/characters/{create['id']}",
        json={
            "name": "Krusty the Clown",
            "actor_id": 1,
        },
    )

    assert res.status_code == 200
    assert res.json()["name"] == "Krusty the Clown"


def test_delete_character_api(client: TestClient) -> None:
    actors_req = client.post(
        "/actors/",
        json={
            "first_name": "Dan",
            "last_name": "Castellaneta",
            "cast": "Main",
        },
    ).json()

    cr_character = client.post(
        "/characters/",
        json={
            "name": "Homer Simpson",
            "actor_id": actors_req["id"],
        },
    ).json()

    res = client.delete(f"/characters/{cr_character['id']}")
    assert res.status_code == 204

    res = client.get(f"/characters/{cr_character['id']}")
    assert res.status_code == 404
