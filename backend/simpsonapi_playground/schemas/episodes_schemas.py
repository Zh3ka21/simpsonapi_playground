from pydantic import BaseModel
from typing import List, Optional

from simpsonapi_playground.schemas.schema import QuoteBase, SeasonBase


class EpisodeBase(BaseModel):
    title: Optional[str] = None
    number: Optional[int] = None
    season_id: Optional[int] = None


class EpisodeCreate(EpisodeBase):
    pass


class EpisodeSchema(EpisodeBase):
    id: int

    model_config = {"from_attributes": True}


class EpisodeResponse(EpisodeBase):
    id: int
    season: Optional[SeasonBase] = None
    quotes: List[QuoteBase] = []

    model_config = {"from_attributes": True}
