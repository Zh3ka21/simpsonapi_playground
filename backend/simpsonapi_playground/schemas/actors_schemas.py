from pydantic import BaseModel
from typing import Optional

from simpsonapi_playground.schemas.characters_schemas import CharacterResponse


class ActorBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    cast: Optional[str] = None


class ActorCreate(ActorBase):
    pass


class ActorGet(ActorBase):
    pass


class ActorSchema(ActorBase):
    id: int

    model_config = {"from_attributes": True}


class ActorResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    cast: str

    characters: list[CharacterResponse]

    model_config = {"from_attributes": True}
