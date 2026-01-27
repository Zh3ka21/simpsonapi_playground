from pydantic import BaseModel
from datetime import date
from typing import Optional


class SeasonBase(BaseModel):
    number: Optional[int] = None
    year_start: Optional[int] = None
    year_end: Optional[int] = None
    season_premiere: Optional[date] = None
    season_finale: Optional[date] = None
    average_viewers: Optional[int] = None
    most_watched_episode_id: Optional[int] = None
    most_watched_episode_viewers: Optional[int] = None


class SeasonCreate(SeasonBase):
    pass


class Season(SeasonBase):
    id: int

    model_config = {"from_attributes": True}
