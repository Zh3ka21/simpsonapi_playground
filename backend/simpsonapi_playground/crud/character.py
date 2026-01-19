from sqlalchemy.orm import Session
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.schemas.schema import CharacterCreate


def create_character(db: Session, data: CharacterCreate):
    new = Character(**data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def get_character(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()


def get_characters(db: Session):
    return db.query(Character).all()


def get_character_by_name(db: Session, char_name=""):
    return db.query(Character).filter(Character.name == char_name).first()
