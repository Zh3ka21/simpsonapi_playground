from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from simpsonapi_playground.core.db import get_db
from simpsonapi_playground.crud.quotes import get_quotes_for_episode
from simpsonapi_playground.schemas.quotes_schemas import (
    PaginatedQuotesResponse,
)

router = APIRouter(prefix="/quotes", tags=["quotes"])


@router.get("/{episode_id}", response_model=PaginatedQuotesResponse)
def get_quotes_for_episode_router(
    episode_id: int, db: Session = Depends(get_db), limit: int = 10, offset: int = 0
):
    return get_quotes_for_episode(db, episode_id, limit=limit, offset=offset)
