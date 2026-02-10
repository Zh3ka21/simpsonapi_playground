from typing import Any, Dict

from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from sqlalchemy.orm import Session

from simpsonapi_playground.models.quote import Quote
from simpsonapi_playground.schemas.quotes_schemas import (
    PaginatedQuotesResponse,
    QuoteCreate,
)
from simpsonapi_playground.utils.batching_utilities import chunked


def get_quotes_for_episode(
    db: Session, episode_id: int, limit: int, offset: int
) -> dict[str, Any]:
    base_query = db.query(Quote).filter(Quote.episode_id == episode_id)
    total = base_query.count()
    items = base_query.offset(offset).limit(limit).all()

    return {
        "items": items,
        "total": total,
        "limit": limit,
        "offset": offset,
    }


def get_character_quotes(
    db: Session, character_id: int, limit: int, offset: int
) -> Dict[str, Any]:
    base_query = db.query(Quote).filter(Quote.character_id == character_id)
    total = base_query.count()
    items = base_query.offset(offset).limit(limit).all()

    return {
        "items": items,
        "total": total,
        "limit": limit,
        "offset": offset,
    }


def get_random_quote(db: Session) -> Quote | None:
    return db.query(Quote).order_by(func.random()).first()


def import_quotes(db: Session, payload: list[QuoteCreate]) -> dict:
    quotes = [Quote(**q.model_dump()) for q in payload]

    try:
        db.bulk_save_objects(quotes)
        db.commit()
        return {"inserted": len(quotes), "skipped": 0}

    except IntegrityError:
        db.rollback()
        return {
            "inserted": 0,
            "skipped": len(quotes),
            "error": "Some quotes already exist",
        }
