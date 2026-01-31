from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from simpsonapi_playground.models.actor import Actor
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.schemas.actors_schemas import ActorCreate


# TODO: Add safe delete
# TODO: Admin role CRUD operations for Actor model
def create_actor(db: Session, data: ActorCreate):
    new = Actor(**data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def read_actors(
    db: Session,
    limit: int,
    offset: int,
    sort: str,
    order: str,
):
    base_query = db.query(Actor)
    total = base_query.count()

    sort_column_map = {
        "id": Actor.id,
        "first_name": Actor.first_name,
        "last_name": Actor.last_name,
        "cast": Actor.cast,
    }
    sort_column = sort_column_map.get(sort, Actor.first_name)
    if order == "asc":
        base_query = base_query.order_by(asc(sort_column), asc(Actor.id))
    else:
        base_query = base_query.order_by(desc(sort_column), asc(Actor.id))

    return (base_query.offset(offset).limit(limit).all(), total)


def read_actor(db: Session, actor_id: int):
    return db.query(Actor).filter(Actor.id == actor_id).first()


def update_actor(db: Session, actor_id: int, data: ActorCreate):
    actor = db.query(Actor).filter(Actor.id == actor_id).first()

    if actor:
        for key, value in data.model_dump().items():
            setattr(actor, key, value)
        db.commit()
        db.refresh(actor)
    return actor


# TODO: Admin role CRUD operations for Actor model
def del_actor(db: Session, character_id: int):
    actor = db.query(Actor).filter(Actor.id == character_id).first()
    db.delete(actor)
    db.commit()


def get_characters_based_on_actor(
    db: Session,
    actor_id: int,
    limit: int,
    offset: int,
):
    base_query = db.query(Character).filter(Character.actor_id == actor_id)

    total = base_query.count()

    items = base_query.order_by(asc(Character.id)).offset(offset).limit(limit).all()

    return items, total


def get_actor_based_on_char(db: Session, character_id: int):
    return db.query(Actor).filter(Actor.id == character_id).all()
