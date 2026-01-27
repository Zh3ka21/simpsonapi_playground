from sqlalchemy.orm import Session
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.models.catchphrase import Catchphrase


def add_catchphrase_to_character(
    db: Session, character_id: int, phrase: str, character: Character
):
    if not character:
        raise ValueError(f"Character with ID {character_id} does not exist.")

    new_catchphrase = Catchphrase(phrase=phrase, character_id=character_id)

    db.add(new_catchphrase)
    db.commit()
    db.refresh(character)

    return new_catchphrase


def get_catchphrases_for_character(
    db: Session, character_id: int, character: Character
):
    if not character:
        raise ValueError(f"Character with ID {character_id} does not exist.")

    return db.query(Catchphrase).filter(Catchphrase.character_id == character_id).all()
