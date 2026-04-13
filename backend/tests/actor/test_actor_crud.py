from calendar import c
from typing import cast
from sqlalchemy.orm import Session

from simpsonapi_playground.api.v1.endpoints import characters
from simpsonapi_playground.crud.actor import create_actor

from simpsonapi_playground.crud.character import (
    create_character,
    del_character,
    get_character,
    get_characters,
    put_character,
)
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.schemas.actors_schemas import ActorCreate
from simpsonapi_playground.models.actor import Actor
from simpsonapi_playground.schemas.characters_schemas import CharacterCreate


def test_create_character(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Dan",
        last_name="Castellaneta",
        cast="Main",
    )

    actor = create_actor(db, actor_data)
    assert actor is not None

    character = create_character(
        db,
        CharacterCreate(
            name="Homer Simpson",
            actor_id=cast(int, actor.id),
        ),
    )
    assert character is not None
    assert character.name == "Homer Simpson"
    assert character.actor_id == actor.id


def test_read_character(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Julie",
        last_name="Kavner",
        cast="Main",
    )
    actor = create_actor(db, actor_data)
    assert actor is not None

    character: CharacterCreate = create_character(
        db,
        CharacterCreate(
            name="Homer Simpson",
            actor_id=cast(int, actor.id),
        ),
    )

    fetched = get_character(db, cast(int, character.id))
    assert fetched is not None
    assert fetched.name == "Homer Simpson"


def test_read_all_characters(db: Session) -> None:
    # Clear existing data
    db.query(Actor).delete()
    db.commit()

    db.query(Character).delete()
    db.commit()

    # Create multiple actors
    actors_data = [
        ActorCreate(first_name="Dan", last_name="Castellaneta", cast="Main"),
    ]

    for data in actors_data:
        create_actor(db, data)

    # Create multiple characters
    characters_data = [
        CharacterCreate(name="Homer Simpson", actor_id=1),
        CharacterCreate(name="Marge Simpson", actor_id=1),
        CharacterCreate(name="Bart Simpson", actor_id=1),
    ]

    for data in characters_data:
        create_character(db, data)

    # Read all characters
    resp = get_characters(db, limit=10, offset=0)

    assert resp["items"] is not None
    assert resp["total"] == 3
    assert len(resp["items"]) == 3

    resp["limit"] == 10
    resp["offset"] == 0

    assert resp["items"][0].name == "Homer Simpson"
    assert resp["items"][1].name == "Marge Simpson"
    assert resp["items"][2].name == "Bart Simpson"


def test_update_character(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Dan",
        last_name="Castellaneta",
        cast="Main",
    )
    actor = create_actor(db, actor_data)
    assert actor is not None

    character = create_character(
        db,
        CharacterCreate(
            name="Bart Simpson",
            actor_id=cast(int, actor.id),
        ),
    )
    assert character is not None
    assert character.name == "Bart Simpson"

    updated_data = CharacterCreate(
        name="Krusty the Clown",
        actor_id=cast(int, actor.id),
    )

    updated = put_character(db, cast(int, actor.id), updated_data)
    assert updated is not None
    assert updated.name == "Krusty the Clown"


def test_delete_character(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Yeardley",
        last_name="Smith",
        cast="Main",
    )
    actor = create_actor(db, actor_data)
    assert actor is not None

    character = create_character(
        db,
        CharacterCreate(
            name="Lisa Simpson",
            actor_id=cast(int, actor.id),
        ),
    )
    assert character is not None

    _ = del_character(db, cast(int, character.id))
    should_be_none = get_character(db, cast(int, character.id))
    assert should_be_none is None
