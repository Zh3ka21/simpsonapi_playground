from typing import Dict, List, Union
from sqlalchemy.orm import Session, selectinload
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.schemas.characters_schemas import CharacterCreate


# TODO: Admin role CRUD operations for Character model
def create_character(db: Session, data: CharacterCreate) -> Character:
    new = Character(**data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def get_character(db: Session, character_id: int) -> Character | None:
    return db.query(Character).filter(Character.id == character_id).first()


def suggest_character_by_name(db: Session, query: str) -> Character | None:
    return (
        db.query(Character)
        .filter(Character.name.ilike(f"%{query}%"))
        .order_by(Character.name.asc())
        .first()
    )


def get_characters(db: Session, limit: int, offset: int):
    base_query = db.query(Character)
    total = base_query.count()

    chars = (
        base_query.options(selectinload(Character.actor))
        .offset(offset)
        .limit(limit)
        .all()
    )
    return {
        "items": chars,
        "total": total,
        "limit": limit,
        "offset": offset,
    }


def get_character_by_name(db: Session, char_name: str = "") -> Character | None:
    return db.query(Character).filter(Character.name == char_name).first()


# TODO: Admin role CRUD operations for Character model
def put_character(
    db: Session, character_id: int, data: CharacterCreate
) -> Character | None:
    character = db.query(Character).filter(Character.id == character_id).first()
    if character:
        for key, value in data.model_dump().items():
            setattr(character, key, value)
        db.commit()
        db.refresh(character)
    return character


# TODO: Admin role CRUD operations for Character model
def del_character(db: Session, character_id: int) -> None:
    character = db.query(Character).filter(Character.id == character_id).first()
    db.delete(character)
    db.commit()
