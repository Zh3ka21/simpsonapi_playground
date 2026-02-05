from http import HTTPStatus
import http
from typing import Any, Dict, Union
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.crud.actor import get_actor_based_on_char
from simpsonapi_playground.crud.quotes import get_character_quotes
from simpsonapi_playground.models.actor import Actor
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.schemas.characters_schemas import (
    CharacterCreate,
    CharacterResponse,
    PaginatedCharacters,
)
from simpsonapi_playground.crud.character import (
    create_character,
    get_character,
    get_character_by_name,
    get_characters,
    put_character,
    del_character,
    suggest_character_by_name,
)
from simpsonapi_playground.schemas.quotes_schemas import (
    PaginatedQuotesResponse,
)
from simpsonapi_playground.schemas.shared_schemas import ActorMini

router = APIRouter(prefix="/characters", tags=["characters"])


@router.post(
    "/",
    response_model=CharacterResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_character_router(
    character: CharacterCreate, db: Session = Depends(get_db)
) -> Character:
    if not character:
        HTTPException(status_code=404, detail="Character data is incorrect")
    return create_character(db, character)


@router.get("/{character_id}", response_model=CharacterResponse)
def read_one_character_router(
    character_id: int, db: Session = Depends(get_db)
) -> Character | None:
    db_character = get_character(db, character_id)
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character


@router.get("/", response_model=Union[PaginatedCharacters, CharacterResponse])
def read_characters_router(
    name_exact: str | None = None,
    q: str | None = None,
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=20),
    offset: int = Query(0, ge=0),
) -> dict[str, list[Character] | int] | Character | None:
    if name_exact:
        character = get_character_by_name(db, name_exact)
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")
        return character

    if q:
        suggested_char = suggest_character_by_name(db, q)
        if not suggested_char:
            raise HTTPException(status_code=404, detail="Character not found")
        return suggested_char

    return get_characters(db, limit, offset)


@router.put("/{char_id}", response_model=CharacterResponse)
def change_character_router(
    char_id: int, data: CharacterCreate, db: Session = Depends(get_db)
) -> Character | None:
    upd_char = put_character(db, char_id, data)
    if not upd_char:
        raise HTTPException(status_code=404, detail="Character was not updated")
    return upd_char


@router.delete(
    "/{char_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_character_router(char_id: int, db: Session = Depends(get_db)) -> int:
    del_character(db, char_id)
    return http.HTTPStatus.NO_CONTENT


@router.get("/{character_id}/actors", response_model=list[ActorMini])
def get_actor_for_character(
    character_id: int,
    db: Session = Depends(get_db),
) -> list[Actor] | None:
    return get_actor_based_on_char(db, character_id)


@router.get("/{character_id}/quotes", response_model=PaginatedQuotesResponse)
def get_characters_quotes_router(
    character_id: int,
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=20),
    offset: int = Query(0, ge=0),
) -> Dict[str, Any] | None:
    return get_character_quotes(db, character_id, limit=limit, offset=offset)
