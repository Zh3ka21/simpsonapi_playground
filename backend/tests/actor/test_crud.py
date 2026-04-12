from typing import cast
from sqlalchemy.orm import Session

from simpsonapi_playground.crud.actor import (
    create_actor,
    del_actor,
    read_actor,
    read_actors,
    update_actor,
)
from simpsonapi_playground.schemas.actors_schemas import ActorCreate
from simpsonapi_playground.models.actor import Actor


def test_create_actor(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Dan",
        last_name="Castellaneta",
        cast="Main",
    )

    actor = create_actor(db, actor_data)
    assert actor is not None

    assert actor.id is not None
    assert actor.first_name == "Dan"
    assert actor.cast == "Main"


def test_read_actor(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Julie",
        last_name="Kavner",
        cast="Main",
    )
    actor = create_actor(db, actor_data)
    assert actor is not None

    fetched = read_actor(db, cast(int, actor.id))
    assert fetched is not None
    assert fetched.id == actor.id
    assert fetched.first_name == "Julie"


def test_read_all_actors(db: Session) -> None:
    # Clear existing actors
    db.query(Actor).delete()
    db.commit()

    # Create multiple actors
    actors_data = [
        ActorCreate(first_name="Dan", last_name="Castellaneta", cast="Main"),
        ActorCreate(first_name="Julie", last_name="Kavner", cast="Main"),
        ActorCreate(first_name="Nancy", last_name="Cartwright", cast="Main"),
    ]

    for data in actors_data:
        create_actor(db, data)

    # Read all actors
    items, total = read_actors(db, limit=10, offset=0, sort="id", order="asc")
    assert items is not None
    assert total == 3
    assert len(items) == 3


def test_update_actor(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Nancy",
        last_name="Cartwright",
        cast="Main",
    )
    actor = create_actor(db, actor_data)
    assert actor is not None

    updated_data: ActorCreate = ActorCreate(
        first_name="Nancy",
        last_name="Cartwright",
        cast="Main",
    )

    updated = update_actor(db, cast(int, actor.id), updated_data)
    assert updated is not None
    assert updated.cast == "Main"


def test_delete_actor(db: Session) -> None:
    actor_data: ActorCreate = ActorCreate(
        first_name="Yeardley",
        last_name="Smith",
        cast="Main",
    )
    actor = create_actor(db, actor_data)
    assert actor is not None

    deleted = del_actor(db, cast(int, actor.id))
    assert deleted is not None
    assert deleted.id == actor.id

    should_be_none = read_actor(db, cast(int, actor.id))
    assert should_be_none is None
