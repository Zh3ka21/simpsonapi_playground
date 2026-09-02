from pydantic import BaseModel
from typing import Optional
from uuid import UUID

from simpsonapi_playground.schemas.shared_schemas import ActorMini


class CharacterBase(BaseModel):
    name: Optional[str] = None
    actor_id: Optional[UUID] = None


class CharacterSchema(CharacterBase):
    id: UUID

    model_config = {"from_attributes": True}


class CharacterCreate(CharacterBase):
    pass


class CharacterResponse(BaseModel):
    id: UUID
    name: str

    actor: ActorMini | None = None

    model_config = {"from_attributes": True}


class PaginatedCharacters(BaseModel):
    items: list[CharacterResponse]
    total: int
    limit: int
    offset: int
