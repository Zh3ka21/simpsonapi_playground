import http
from typing import Dict, List, Union
from sqlalchemy import func
from sqlalchemy.orm import Session, selectinload
from simpsonapi_playground.models.episode import Episode
from simpsonapi_playground.schemas.episodes_schemas import EpisodeCreate


# TODO: Admin role CRUD operations for Character model
def create_episode(db: Session, data: EpisodeCreate) -> Episode | None:
    new = Episode(**data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def get_episode(db: Session, episode_id: int) -> Episode | None:
    return db.query(Episode).filter(Episode.id == episode_id).first()


def get_episodes(db: Session, limit: int = 10, offset: int = 0):
    base_query = db.query(Episode).options(
        selectinload(Episode.season), selectinload(Episode.quotes)
    )
    total = base_query.count()
    items = base_query.limit(limit).offset(offset).all()

    return {
        "items": items,
        "total": total,
        "limit": limit,
        "offset": offset,
    }


def get_episode_by_name(db: Session, episode_title: str = "") -> Episode | None:
    return db.query(Episode).filter(Episode.title == episode_title).first()


# TODO: Admin role CRUD operations for Character model
def put_episode(db: Session, episode_id: int, data: EpisodeCreate) -> Episode | None:
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    if episode:
        for key, value in data.model_dump().items():
            setattr(episode, key, value)
        db.commit()
        db.refresh(episode)
    return episode


# TODO: Admin role CRUD operations for Character model
def del_episode(db: Session, episode_id: int) -> http.HTTPStatus:
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    db.delete(episode)
    db.commit()
    return http.HTTPStatus.NO_CONTENT


def select_random_episode(db: Session) -> Episode | None:
    return db.query(Episode).order_by(func.random()).first()


def get_season_by_episode(db: Session, episode_id: int) -> Episode | None:
    return (
        db.query(Episode)
        .options(selectinload(Episode.season))
        .filter(Episode.id == episode_id)
        .first()
    )


def get_episodes_by_season(
    db: Session, season_id: int, limit: int = 10, offset: int = 0
):
    base_query = (
        db.query(Episode)
        .options(selectinload(Episode.season))
        .filter(Episode.season_id == season_id)
    )
    total = base_query.count()
    items = base_query.limit(limit).offset(offset).all()

    return {
        "items": items,
        "total": total,
        "limit": limit,
        "offset": offset,
    }
