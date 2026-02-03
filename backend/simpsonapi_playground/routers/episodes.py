from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db

from simpsonapi_playground.schemas.episodes_schemas import (
    EpisodeCreate,
    EpisodeResponse,
    EpisodeSchema,
    PaginatedEpisodes,
)
from simpsonapi_playground.crud.episode import (
    create_episode,
    get_episode,
    get_episodes,
    get_episode_by_name,
    get_season_by_episode,
    put_episode,
    del_episode,
    select_random_episode,
)

router = APIRouter(prefix="/episodes", tags=["episodes"])


@router.post("/", response_model=EpisodeSchema, status_code=status.HTTP_201_CREATED)
def create_episode_router(episode: EpisodeCreate, db: Session = Depends(get_db)):
    return create_episode(db, episode)


@router.get("/random", response_model=EpisodeResponse)
def get_random_episode_router(db: Session = Depends(get_db)):
    return select_random_episode(db)


@router.get("/{episode_id}", response_model=EpisodeResponse)
def get_episode_router(episode_id: int, db: Session = Depends(get_db)):
    db_episode = get_episode(db, episode_id)
    if not db_episode:
        raise HTTPException(status_code=404, detail="Episode not found")
    return db_episode


@router.get("/", response_model=PaginatedEpisodes)
def get_episodes_router(
    db: Session = Depends(get_db),
    title: str | None = None,
    limit: int = 10,
    offset: int = 0,
):
    if title:
        episode = get_episode_by_name(db, title)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")
        return [episode]
    return get_episodes(db, limit=limit, offset=offset)


@router.put("/{episode_id}", response_model=EpisodeResponse)
def update_episode_router(
    episode_id: int, data: EpisodeCreate, db: Session = Depends(get_db)
):
    upd_episode = put_episode(db, episode_id, data)
    if not upd_episode:
        raise HTTPException(status_code=404, detail="Episode was not updated")
    return upd_episode


@router.delete("/{episode_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_episode(episode_id: int = None, db: Session = Depends(get_db)):
    del_episode(db, episode_id)


# TODO: episode description/request to get more details on episodes
@router.get("/{episode_id}/season")
def get_season_by_episode_router(episode_id: int, db: Session = Depends(get_db)):
    return get_season_by_episode(db, episode_id)
