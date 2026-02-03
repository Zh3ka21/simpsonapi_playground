from sqlalchemy import func
from sqlalchemy.orm import Session

from simpsonapi_playground.models.quote import Quote


def get_quotes_for_episode(db: Session, episode_id: int, limit: int, offset: int):
    base_query = db.query(Quote).filter(Quote.episode_id == episode_id)
    total = base_query.count()
    items = base_query.offset(offset).limit(limit).all()

    return {
        "items": items,
        "total": total,
        "limit": limit,
        "offset": offset,
    }


def get_character_quotes(db: Session, character_id: int, limit: int, offset: int):
    base_query = db.query(Quote).filter(Quote.character_id == character_id)
    total = base_query.count()
    items = base_query.offset(offset).limit(limit).all()

    return {
        "items": items,
        "total": total,
        "limit": limit,
        "offset": offset,
    }


def get_random_quote(db: Session):
    return db.query(Quote).order_by(func.random()).first()
