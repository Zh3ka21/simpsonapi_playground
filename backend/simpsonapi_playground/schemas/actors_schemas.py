from pydantic import BaseModel
from typing import Optional

from simpsonapi_playground.schemas.shared_schemas import CharacterMini


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

    characters: list[CharacterMini] = []

    model_config = {"from_attributes": True}


class PaginatedActors(BaseModel):
    items: list[ActorSchema]
    total: int
    limit: int
    offset: int
