from typing import Optional
from pydantic import BaseModel

from simpsonapi_playground.schemas.shared_schemas import CharacterMini


class QuoteBase(BaseModel):
    quote: Optional[str] = None
    episode_id: Optional[int] = None
    character_id: Optional[int] = None


class QuoteCreate(QuoteBase):
    pass


class QuoteResponse(BaseModel):
    quote: Optional[str] = None

    character_id: Optional[int] = None
    episode_id: Optional[int] = None

    character: CharacterMini | None = None
    model_config = {"from_attributes": True}


class PaginatedQuotesResponse(BaseModel):
    total: int
    limit: int
    offset: int
    items: list[QuoteResponse]

    model_config = {"from_attributes": True}
