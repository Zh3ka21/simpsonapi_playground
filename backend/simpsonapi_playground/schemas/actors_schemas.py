from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class ActorBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    cast: Optional[str] = None


class ActorCreate(ActorBase):
    pass


class ActorSchema(ActorBase):
    id: UUID

    model_config = {"from_attributes": True}


class PaginatedActors(BaseModel):
    items: list[ActorSchema]
    total: int
    limit: int
    offset: int
