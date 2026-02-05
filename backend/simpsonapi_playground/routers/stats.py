from typing import Any
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
def most_quoted_character(
    db: Session = Depends(get_db),
) -> dict[str, Any] | None:
    quoted_char = get_most_quoted_character(db)
    if not quoted_char:
        return None
    return quoted_char


@router.get("/episode/most-quoted", response_model=StatsEpisodeMostQuoted)
def most_quoted_episode(db: Session = Depends(get_db)) -> dict[str, Any] | None:
    quoted_episode = get_most_quoted_episode(db)
    if not quoted_episode:
        return None
    return quoted_episode
