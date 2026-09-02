from typing import Dict, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from simpsonapi_playground.core.session import get_db
from simpsonapi_playground.crud.episode import get_episodes_by_season
from simpsonapi_playground.models.episode import Episode
from simpsonapi_playground.schemas.episodes_schemas import (
    EpisodeSchema,
    PaginatedEpisodes,
)

router = APIRouter(prefix="/seasons", tags=["episodes"])


@router.get("/{season_id}/episodes", response_model=PaginatedEpisodes)
def get_episodes_by_season_router(
    season_id: UUID, db: Session = Depends(get_db), limit: int = 10, offset: int = 0
) -> PaginatedEpisodes:
    episodes = get_episodes_by_season(db, season_id, limit=limit, offset=offset)

    return PaginatedEpisodes(
        items=[EpisodeSchema.model_validate(episode) for episode in episodes["items"]],
        total=episodes["total"],
        limit=episodes["limit"],
        offset=episodes["offset"],
    )
