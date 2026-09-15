from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from pydantic import Field

from simpsonapi_playground.schemas.seasons_schemas import SeasonBase
from simpsonapi_playground.schemas.quotes_schemas import QuoteBase


class EpisodeBase(BaseModel):
    title: Optional[str] = None
    number: Optional[int] = None
    season_id: Optional[UUID] = None


class EpisodeCreate(EpisodeBase):
    pass


class EpisodeSchema(EpisodeBase):
    id: UUID

    model_config = {"from_attributes": True}


class PaginatedEpisodes(BaseModel):
    items: List[EpisodeSchema]
    total: int
    limit: int
    offset: int


class EpisodeResponse(EpisodeBase):
    id: UUID
    season: Optional[SeasonBase] = None
    quotes: list[QuoteBase] = Field(default_factory=list)

    model_config = {"from_attributes": True}
