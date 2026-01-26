from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.crud.actor import (
    create_actor,
    del_actor,
    get_character_based_on_actor,
    read_actor,
    read_actors,
    update_actor,
)
from simpsonapi_playground.schemas.actors_schemas import (
    ActorSchema,
    ActorCreate,
    ActorResponse,
)
from simpsonapi_playground.schemas.shared_schemas import ActorMini

router = APIRouter(prefix="/actors", tags=["actors"])


@router.post("/", response_model=ActorSchema)
def create_an_actor(actor: ActorCreate, db: Session = Depends(get_db)):
    return create_actor(db, actor)


@router.get("/", response_model=list[ActorMini])
def read_all_actors(db: Session = Depends(get_db)):
    return read_actors(db)


@router.get("/{actor_id}", response_model=ActorSchema)
def read_an_actor(actor_id: int, db: Session = Depends(get_db)):
    return read_actor(db, actor_id)


@router.put("/{actor_id}", response_model=ActorSchema)
def upd_actor(actor_id: int, data: ActorCreate, db: Session = Depends(get_db)):
    upd_actor = update_actor(db, actor_id, data)
    if not upd_actor:
        raise HTTPException(status_code=404, detail="Character was not updated")
    return upd_actor


@router.delete("/{actor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_actor(actor_id: int, db: Session = Depends(get_db)):
    del_actor(db, actor_id)


@router.get("/{actor_id}/characters", response_model=ActorResponse)
def get_characters_played_by_actor(db: Session = Depends(get_db), actor_id: int = None):
    return get_character_based_on_actor(db, actor_id)
