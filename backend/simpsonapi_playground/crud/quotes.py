from sqlalchemy import func
from sqlalchemy.orm import Session

from simpsonapi_playground.models.quote import Quote


def get_quotes_for_episode(db: Session, episode_id: int):
    return db.query(Quote).filter(Quote.episode_id == episode_id).all()


def get_character_quotes(db: Session, character_id: int):
    return db.query(Quote).filter(Quote.character_id == character_id).all()


def get_random_quote(db: Session):
    return db.query(Quote).order_by(func.random()).first()
