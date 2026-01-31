from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.crud.actor import get_actor_based_on_char
from simpsonapi_playground.crud.quotes import get_character_quotes
from simpsonapi_playground.schemas.characters_schemas import (
    CharacterCreate,
    CharacterResponse,
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
from simpsonapi_playground.schemas.quotes_schemas import QuoteResponse
from simpsonapi_playground.schemas.shared_schemas import ActorMini

router = APIRouter(prefix="/characters", tags=["characters"])


@router.post(
    "/",
    response_model=CharacterResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_character_router(character: CharacterCreate, db: Session = Depends(get_db)):
    return create_character(db, character)


@router.get("/{character_id}", response_model=CharacterResponse)
def read_one_character_router(character_id: int, db: Session = Depends(get_db)):
    db_character = get_character(db, character_id)
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character


@router.get("/", response_model=list[CharacterResponse])
def read_characters_router(
    name_exact: str | None = None,
    q: str | None = None,
    db: Session = Depends(get_db),
):
    if name_exact:
        character = get_character_by_name(db, name_exact)
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")
        return [character]

    if q:
        return [suggest_character_by_name(db, q)]

    return get_characters(db)


@router.put("/{char_id}", response_model=CharacterResponse)
def change_character_router(
    char_id: int = None, data: CharacterCreate = None, db: Session = Depends(get_db)
):
    upd_char = put_character(db, char_id, data)
    if not upd_char:
        raise HTTPException(status_code=404, detail="Character was not updated")
    return upd_char


@router.delete(
    "/{char_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_character_router(char_id: int = None, db: Session = Depends(get_db)):
    del_character(db, char_id)


@router.get("/{character_id}/actors", response_model=list[ActorMini])
def get_actors_for_character(
    character_id: int,
    db: Session = Depends(get_db),
):
    return get_actor_based_on_char(db, character_id)


@router.get("/{character_id}/quotes", response_model=list[QuoteResponse])
def get_characters_quotes_router(character_id: int, db: Session = Depends(get_db)):
    return get_character_quotes(db, character_id)
