from os import name
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from simpsonapi_playground.crud.actor import create_actor
from simpsonapi_playground.crud.character import create_character
from simpsonapi_playground.schemas.actors_schemas import ActorCreate
from simpsonapi_playground.schemas.characters_schemas import CharacterCreate


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


def test_get_characters_played_by_actor(db: Session, client: TestClient) -> None:

    # Create an actor to associate characters with
    actor_data: ActorCreate = ActorCreate(
        first_name="Dan",
        last_name="Castellaneta",
        cast="Main",
    )

    actor = create_actor(db, actor_data)
    assert actor is not None

    # Create multiple actors
    characters_data = [
        CharacterCreate(name="Homer Simpson", actor_id=int(actor.id)),
        CharacterCreate(name="Abe Simpson", actor_id=int(actor.id)),
        CharacterCreate(name="Krusty the Clown", actor_id=int(actor.id)),
    ]

    for cdata in characters_data:
        char = create_character(db, cdata)
        assert char is not None

    response = client.get(
        f"/actors/{actor.id}/characters",
        params={"limit": 10, "offset": 0},
    ).json()

    assert response is not None
    print(response)

    assert response["total"] == 3

    assert response["items"] is not None
    assert response["items"][0]["name"] == "Homer Simpson"

    assert response["items"][0]["actor"] is not None
    assert response["items"][0]["actor"]["first_name"] == "Dan"
