from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.schemas.characters_schemas import (
    Character,
    CharacterCreate,
    CharacterGet,
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


@router.post("/", response_model=Character)
def create_char(character: CharacterCreate, db: Session = Depends(get_db)):
    return create_character(db, character)


@router.get("/id/{character_id}", response_model=Character)
def read_one(character_id: int, db: Session = Depends(get_db)):
    db_character = get_character(db, character_id)
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character


@router.get("/", response_model=list[Character])
def read_all(db: Session = Depends(get_db)):
    return get_characters(db)


@router.get("/name/{char_name}", response_model=CharacterGet)
def read_one_by_name(char_name: str, db: Session = Depends(get_db)):
    db_character = get_character_by_name(db, char_name)
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character


@router.put("/{char_id}", response_model=Character)
def change_character(
    char_id: int = None, data: CharacterCreate = None, db: Session = Depends(get_db)
):
    upd_char = put_character(db, char_id, data)
    if not upd_char:
        raise HTTPException(status_code=404, detail="Character was not updated")
    return upd_char


@router.delete("/{char_id}", status_code=204)
def delete_character(char_id: int = None, db: Session = Depends(get_db)):
    del_character(db, char_id)
