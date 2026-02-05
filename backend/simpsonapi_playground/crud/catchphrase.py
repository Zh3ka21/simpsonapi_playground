from typing import Dict, List, Union
from sqlalchemy.orm import Session
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.models.catchphrase import Catchphrase
from simpsonapi_playground.schemas.catchphrase_schemas import CatchphraseResponse


def add_catchphrase_to_character(
    db: Session, character_id: int, phrase: str, character: Character
) -> Catchphrase | None:
    if not character:
        raise ValueError(f"Character with ID {character_id} does not exist.")

    new_catchphrase = Catchphrase(phrase=phrase, character_id=character_id)

    db.add(new_catchphrase)
    db.commit()
    db.refresh(new_catchphrase)

    return new_catchphrase


def get_catchphrases_for_character(
    db: Session,
    character_id: int,
    character: Character,
    limit: int,
    offset: int,
):
    if not character:
        raise ValueError(f"Character with ID {character_id} does not exist.")

    base_query = db.query(Catchphrase).filter(Catchphrase.character_id == character_id)
    total = base_query.count()

    catchphrases = base_query.order_by(Catchphrase.id).offset(offset).limit(limit).all()

    return {
        "items": catchphrases,
        "total": total,
        "limit": limit,
        "offset": offset,
    }
