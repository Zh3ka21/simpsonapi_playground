from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.crud import episode
from simpsonapi_playground.schemas.episodes_schemas import (
    EpisodeBase,
    EpisodeCreate,
    EpisodeResponse,
    EpisodeSchema,
)
from simpsonapi_playground.crud.episode import (
    create_episode,
    get_episode,
    get_episodes,
    get_episode_by_name,
    get_episodes_by_season,
    get_season_by_episode,
    put_episode,
    del_episode,
    select_random_episode,
)

router = APIRouter(prefix="/episodes", tags=["episodes"])


@router.post("/", response_model=EpisodeSchema)
def create_episode_router(character: EpisodeCreate, db: Session = Depends(get_db)):
    return create_episode(db, character)


@router.get("/id/{episode_id}", response_model=EpisodeSchema)
def get_episode_router(episode_id: int, db: Session = Depends(get_db)):
    db_episode = get_episode(db, episode_id)
    if not db_episode:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_episode


@router.get("/", response_model=list[EpisodeResponse])
def get_episodes_router(db: Session = Depends(get_db)):
    return get_episodes(db)


@router.get("/name/{episode_title}", response_model=EpisodeResponse)
def get_episode_by_name_router(episode_title: str, db: Session = Depends(get_db)):
    db_episode = get_episode_by_name(db, episode_title)
    if not db_episode:
        raise HTTPException(status_code=404, detail="Episode not found")
    return db_episode


@router.put("/{episode_id}", response_model=EpisodeResponse)
def update_episode_router(
    episode_id: int = None, data: EpisodeCreate = None, db: Session = Depends(get_db)
):
    upd_episode = put_episode(db, episode_id, data)
    if not upd_episode:
        raise HTTPException(status_code=404, detail="Episode was not updated")
    return upd_episode


@router.delete("/{episode_id}", status_code=204)
def delete_character(episode_id: int = None, db: Session = Depends(get_db)):
    del_episode(db, episode_id)


# TODO: episode description/request to get more details on episodes
@router.get("/season/{season_id}", response_model=list[EpisodeResponse])
def get_episodes_by_season_router(season_id: int = None, db: Session = Depends(get_db)):
    episodes = get_episodes_by_season(db, season_id)
    return episodes


# TODO: episode description/request to get more details on episodes
@router.get("/episode/{episode_id}", response_model=list[EpisodeResponse])
def get_season_by_episode_router(episode_id: int = None, db: Session = Depends(get_db)):
    return get_season_by_episode(db, episode_id)


@router.get("/episode/", response_model=EpisodeResponse)
def get_random_episode_router(db: Session = Depends(get_db)):
    return select_random_episode(db)
