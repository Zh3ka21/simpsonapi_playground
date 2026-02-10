from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.crud.quotes import get_quotes_for_episode, import_quotes
from simpsonapi_playground.schemas.quotes_schemas import (
    PaginatedQuotesResponse,
    QuoteCreate,
)

router = APIRouter(prefix="/quotes", tags=["quotes"])


@router.get("/{episode_id}", response_model=PaginatedQuotesResponse)
def get_quotes_for_episode_router(
    episode_id: int, db: Session = Depends(get_db), limit: int = 10, offset: int = 0
) -> dict[str, Any]:
    return get_quotes_for_episode(db, episode_id, limit=limit, offset=offset)


@router.post("/bulk", status_code=201)
def import_quotes_router(
    payload: list[QuoteCreate],
    db: Session = Depends(get_db),
):
    count = import_quotes(db, payload)
    return {"inserted": count}
