from sqlalchemy.orm import Session, selectinload
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.schemas.characters_schemas import CharacterCreate


# TODO: Admin role CRUD operations for Character model
def create_character(db: Session, data: CharacterCreate):
    new = Character(**data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def get_character(db: Session, character_id: str):
    return db.query(Character).filter(Character.id == character_id).first()


def get_characters(db: Session):
    return db.query(Character).options(selectinload(Character.actor)).all()


def get_character_by_name(db: Session, char_name=""):
    return db.query(Character).filter(Character.name == char_name).first()


# TODO: Admin role CRUD operations for Character model
def put_character(db: Session, character_id: int, data: CharacterCreate):
    character = db.query(Character).filter(Character.id == character_id).first()
    if character:
        for key, value in data.model_dump().items():
            setattr(character, key, value)
        db.commit()
        db.refresh(character)
    return character


# TODO: Admin role CRUD operations for Character model
def del_character(db: Session, character_id: int):
    character = db.query(Character).filter(Character.id == character_id).first()
    db.delete(character)
    db.commit()
