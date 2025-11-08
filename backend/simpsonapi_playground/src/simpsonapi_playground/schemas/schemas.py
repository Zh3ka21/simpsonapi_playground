from pydantic import BaseModel
from datetime import date
from typing import Optional


class ActorBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    cast: Optional[str] = None


class ActorCreate(ActorBase):
    pass


class Actor(ActorBase):
    id: int

    class Config:
        orm_mode = True


class CharacterBase(BaseModel):
    name: Optional[str] = None
    actor_id: Optional[int] = None


class CharacterCreate(CharacterBase):
    pass


class Character(CharacterBase):
    id: int

    class Config:
        orm_mode = True


class CatchphraseBase(BaseModel):
    phrase: Optional[str] = None
    character_id: Optional[int] = None


class CatchphraseCreate(CatchphraseBase):
    pass


class Catchphrase(CatchphraseBase):
    id: int

    class Config:
        orm_mode = True


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

    class Config:
        orm_mode = True


class EpisodeBase(BaseModel):
    title: Optional[str] = None
    episode_no: Optional[int] = None
    production_code: Optional[str] = None
    air_date: Optional[date] = None
    us_viewers: Optional[int] = None
    season_id: Optional[int] = None


class EpisodeCreate(EpisodeBase):
    pass


class Episode(EpisodeBase):
    id: int

    class Config:
        orm_mode = True


class QuoteBase(BaseModel):
    quote: Optional[str] = None
    episode_id: Optional[int] = None
    character_id: Optional[int] = None


class QuoteCreate(QuoteBase):
    pass


class Quote(QuoteBase):
    id: int

    class Config:
        orm_mode = True
