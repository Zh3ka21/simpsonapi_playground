# tests/test_actor_crud.py
from typing import cast
from sqlalchemy.orm import Session

from simpsonapi_playground.crud.actor import (
    create_actor,
    del_actor,
    read_actor,
    update_actor,
)
from simpsonapi_playground.schemas.actors_schemas import ActorCreate
from simpsonapi_playground.models.actor import Actor


def test_create_actor(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Dan",
        last_name="Castellaneta",
        cast="Homer",
    )

    actor = create_actor(db, actor_data)
    assert actor is not None

    assert actor.id is not None
    assert actor.first_name == "Dan"


def test_read_actor(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Julie",
        last_name="Kavner",
        cast="Marge",
    )
    actor = create_actor(db, actor_data)
    assert actor is not None

    fetched = read_actor(db, cast(int, actor.id))
    assert fetched is not None
    assert fetched.id == actor.id
    assert fetched.first_name == "Julie"


def test_update_actor(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Nancy",
        last_name="Cartwright",
        cast="Bart",
    )
    actor = create_actor(db, actor_data)
    assert actor is not None

    updated_data: ActorCreate = ActorCreate(
        first_name="Nancy",
        last_name="Cartwright",
        cast="Bart Simpson",
    )

    updated = update_actor(db, cast(int, actor.id), updated_data)
    assert updated is not None
    assert updated.cast == "Bart Simpson"


def test_delete_actor(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Yeardley",
        last_name="Smith",
        cast="Lisa",
    )
    actor = create_actor(db, actor_data)
    assert actor is not None

    deleted = del_actor(db, cast(int, actor.id))
    assert deleted is not None
    assert deleted.id == actor.id

    should_be_none = read_actor(db, cast(int, actor.id))
    assert should_be_none is None
