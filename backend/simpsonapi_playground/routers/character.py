from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.schemas.schema import Character, CharacterCreate
from simpsonapi_playground.crud.character import (
    create_character,
    get_character,
    get_characters
)

router = APIRouter(
    prefix="/characters",
    tags=["characters"]
)

@router.post("/", response_model=Character)
def create(character: CharacterCreate, db: Session = Depends(get_db)):
    return create_character(db, character)

@router.get("/{character_id}", response_model=Character)
def read_one(character_id: int, db: Session = Depends(get_db)):
    db_character = get_character(db, character_id)
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

@router.get("/", response_model=list[Character])
def read_all(db: Session = Depends(get_db)):
    return get_characters(db)

@router.get("/{char_name}", response_model=Character)
def read_one_by_name(char_name: str, db: Session = Depends(get_db)):
    db_character = get_character(db, char_name)
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character 
