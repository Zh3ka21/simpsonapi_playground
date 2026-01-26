from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.schemas.characters_schemas import (
    Character,
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
)

router = APIRouter(prefix="/characters", tags=["characters"])


@router.post(
    "/",
    response_model=Character,
    status_code=status.HTTP_201_CREATED,
)
def create_character_router(character: CharacterCreate, db: Session = Depends(get_db)):
    return create_character(db, character)


@router.get("/{character_id}", response_model=Character)
def read_one_character_router(character_id: int, db: Session = Depends(get_db)):
    db_character = get_character(db, character_id)
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character


@router.get("/", response_model=list[CharacterResponse])
def read_characters_router(
    name: str | None = None,
    db: Session = Depends(get_db),
):
    if name:
        character = get_character_by_name(db, name)
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")
        return [character]
    return get_characters(db)


@router.put("/{char_id}", response_model=Character)
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
