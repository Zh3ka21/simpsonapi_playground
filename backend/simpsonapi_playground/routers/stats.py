from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.crud.stat import (
    get_most_quoted_character,
    get_most_quoted_episode,
)
from simpsonapi_playground.schemas.shared_schemas import (
    StatsCharacterMostQuoted,
    StatsEpisodeMostQuoted,
)


router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/character/most-quoted", response_model=StatsCharacterMostQuoted)
def most_quoted_character(db: Session = Depends(get_db)):
    return get_most_quoted_character(db)


@router.get("/episode/most-quoted", response_model=StatsEpisodeMostQuoted)
def most_quoted_episode(db: Session = Depends(get_db)):
    return get_most_quoted_episode(db)
