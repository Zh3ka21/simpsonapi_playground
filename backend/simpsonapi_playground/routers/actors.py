from typing import Any, Dict, Tuple, Literal
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.crud.actor import (
    create_actor,
    del_actor,
    get_characters_based_on_actor,
    read_actor,
    read_actors,
    update_actor,
)
from simpsonapi_playground.models.actor import Actor
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.schemas.actors_schemas import (
    ActorSchema,
    ActorCreate,
    PaginatedActors,
)
from simpsonapi_playground.schemas.characters_schemas import PaginatedCharacters

router = APIRouter(prefix="/actors", tags=["actors"])


@router.post("/", response_model=ActorSchema)
def create_an_actor(actor: ActorCreate, db: Session = Depends(get_db)) -> ActorSchema:
    new_actor = create_actor(db, actor)
    if new_actor is None:
        raise HTTPException(status_code=400, detail="Actor data was incorrect")
    return ActorSchema.model_validate(new_actor)


@router.get("/", response_model=PaginatedActors)
def read_all_actors(
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=20),
    offset: int = Query(0, ge=0),
    sort: str = Query("id", pattern="^(id|first_name|last_name|cast)$"),
    order: Literal["asc", "desc"] = Query("asc", pattern="^(asc|desc)$"),
) -> Dict[str, Any]:
    items, total = read_actors(db, limit=limit, offset=offset, sort=sort, order=order)
    return {"items": items, "total": total, "limit": limit, "offset": offset}


@router.get("/{actor_id}", response_model=ActorSchema)
def read_an_actor(actor_id: int, db: Session = Depends(get_db)) -> ActorSchema:
    actor = read_actor(db, actor_id)
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor


@router.put("/{actor_id}", response_model=ActorSchema)
def upd_actor(
    actor_id: int, data: ActorCreate, db: Session = Depends(get_db)
) -> Actor | None:
    upd_actor = update_actor(db, actor_id, data)
    if not upd_actor:
        raise HTTPException(status_code=404, detail="Actor was not updated")
    return upd_actor


# TODO: Referential integrity (prevent deleting actors with characters), Safe delete
@router.delete("/{actor_id}", status_code=204)
def delete_actor(actor_id: int, db: Session = Depends(get_db)) -> None:
    deleted = del_actor(db, actor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Actor not found")
    return None


@router.get("/{actor_id}/characters", response_model=PaginatedCharacters)
def get_characters_played_by_actor(
    db: Session = Depends(get_db),
    actor_id: int = 0,
    limit: int = Query(10, ge=1, le=20),
    offset: int = Query(0, ge=0),
) -> Dict[str, Any]:
    items, total = get_characters_based_on_actor(
        db, actor_id, limit=limit, offset=offset
    )

    return {
        "items": items,
        "total": total,
        "limit": limit,
        "offset": offset,
    }
