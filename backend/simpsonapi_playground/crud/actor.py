from sqlalchemy.orm import Session, selectinload

from simpsonapi_playground.models.actor import Actor
from simpsonapi_playground.schemas.actors_schemas import ActorCreate, ActorResponse


# TODO: Admin role CRUD operations for Actor model
def create_actor(db: Session, data: ActorCreate):
    new = Actor(**data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def read_actors(db: Session):
    return db.query(Actor).all()


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


def get_character_based_on_actor(db: Session, actor_id: int) -> ActorResponse:
    return (
        db.query(Actor)
        .options(selectinload(Actor.characters))
        .filter(Actor.id == actor_id)
        .first()
    )


def get_actor_based_on_char(db: Session, character_id: int):
    return db.query(Actor).filter(Actor.id == character_id).all()
