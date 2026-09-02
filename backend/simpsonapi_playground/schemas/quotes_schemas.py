from typing import Optional
from pydantic import BaseModel
from uuid import UUID

from simpsonapi_playground.schemas.shared_schemas import CharacterMini


class QuoteBase(BaseModel):
    quote: Optional[str] = None
    episode_id: Optional[UUID] = None
    character_id: Optional[UUID] = None


class QuoteCreate(QuoteBase):
    pass


class QuoteResponse(QuoteBase):
    character: CharacterMini | None = None
    model_config = {"from_attributes": True}


class PaginatedQuotesResponse(BaseModel):
    total: int
    limit: int
    offset: int
    items: list[QuoteResponse]

    model_config = {"from_attributes": True}
