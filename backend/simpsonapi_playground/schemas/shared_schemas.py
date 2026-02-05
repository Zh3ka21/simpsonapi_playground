from pydantic import BaseModel


class ActorMini(BaseModel):
    id: int
    first_name: str
    last_name: str

    model_config = {"from_attributes": True}


class CharacterMini(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


class EpisodeMini(BaseModel):
    title: str
    number: int
    season_id: int


class StatsCharacterMostQuoted(BaseModel):
    character: CharacterMini
    quote_count: int


class StatsEpisodeMostQuoted(BaseModel):
    episode: EpisodeMini
    quote_count: int
