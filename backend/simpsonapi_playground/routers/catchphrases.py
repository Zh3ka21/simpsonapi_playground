from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db

from simpsonapi_playground.crud.character import get_character
from simpsonapi_playground.schemas.catchphrase_schemas import CatchphraseSchema
from simpsonapi_playground.crud.catchphrase import (
    add_catchphrase_to_character,
    get_catchphrases_for_character,
)


router = APIRouter(prefix="/catchphrases", tags=["catchphrases"])


@router.post(
    "/{character_id}/catchphrase",
    status_code=status.HTTP_201_CREATED,
    response_model=CatchphraseSchema,
)
def add_catchphrase_to_character_router(
    character_id: int,
    catchphrase: str,
    db: Session = Depends(get_db),
):
    character = get_character(db, character_id)
    return add_catchphrase_to_character(db, character_id, catchphrase, character)


@router.get("/{character_id}/catchphrase", response_model=list[CatchphraseSchema])
def get_catchphrases_for_character_router(
    character_id: int,
    db: Session = Depends(get_db),
):
    character = get_character(db, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return get_catchphrases_for_character(db, character_id, character)
