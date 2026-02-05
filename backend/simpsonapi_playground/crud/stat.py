from sqlalchemy.orm import Session
from sqlalchemy import func

from simpsonapi_playground.models.character import Character
from simpsonapi_playground.models.episode import Episode
from simpsonapi_playground.models.quote import Quote


def get_most_quoted_character(
    db: Session,
):
    base_query = (
        db.query(Quote)
        .group_by(Quote.character_id)
        .order_by(func.count(Quote.id).desc())
        .first()
    )
    if base_query:
        character_id = base_query.character_id
        quote_count = db.query(Quote).filter(Quote.character_id == character_id).count()
        character = db.query(Character).filter(Character.id == character_id).first()
        return {
            "character": character,
            "quote_count": quote_count,
        }


def get_most_quoted_episode(db: Session):
    base_query = (
        db.query(Quote)
        .group_by(Quote.episode_id)
        .order_by(func.count(Quote.id).desc())
        .first()
    )
    if base_query:
        episode_id = base_query.episode_id
        quote_count = db.query(Quote).filter(Quote.episode_id == episode_id).count()
        episode = db.query(Episode).filter(Episode.id == episode_id).first()
        return {
            "episode": episode,
            "quote_count": quote_count,
        }
