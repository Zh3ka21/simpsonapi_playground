from pydantic import BaseModel
from uuid import UUID


class ActorMini(BaseModel):
    id: UUID
    first_name: str
    last_name: str

    model_config = {"from_attributes": True}


class CharacterMini(BaseModel):
    id: UUID
    name: str

    model_config = {"from_attributes": True}


class EpisodeMini(BaseModel):
    title: str
    number: int
    season_id: UUID


class StatsCharacterMostQuoted(BaseModel):
    character: CharacterMini
    quote_count: int


class StatsEpisodeMostQuoted(BaseModel):
    episode: EpisodeMini
    quote_count: int
