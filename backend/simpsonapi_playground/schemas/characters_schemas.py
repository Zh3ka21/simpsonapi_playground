from pydantic import BaseModel
from typing import Optional

from simpsonapi_playground.schemas.shared_schemas import ActorMini


class CharacterBase(BaseModel):
    name: Optional[str] = None
    actor_id: Optional[int] = None


class CharacterCreate(CharacterBase):
    pass


class Character(CharacterBase):
    id: int

    model_config = {"from_attributes": True}


class CharacterResponse(BaseModel):
    id: int
    name: str

    actor: ActorMini | None = None

    model_config = {"from_attributes": True}
