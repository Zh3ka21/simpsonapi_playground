from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.crud.episode import get_episodes_by_season
from simpsonapi_playground.schemas.episodes_schemas import (
    PaginatedEpisodes,
)

router = APIRouter(prefix="/seasons", tags=["episodes"])


@router.get("/{season_id}/episodes", response_model=PaginatedEpisodes)
def get_episodes_by_season_router(
    season_id: int, db: Session = Depends(get_db), limit: int = 10, offset: int = 0
):
    return get_episodes_by_season(db, season_id, limit=limit, offset=offset)
