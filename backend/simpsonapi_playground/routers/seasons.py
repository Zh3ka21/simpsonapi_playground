from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.schemas.episodes_schemas import EpisodeSchema

router = APIRouter(prefix="/seasons", tags=["episodes"])


@router.get("/{season_id}/episodes", response_model=list[EpisodeSchema])
def get_episodes_by_season(season_id: int, db: Session = Depends(get_db)):
    return get_episodes_by_season(db, season_id)
