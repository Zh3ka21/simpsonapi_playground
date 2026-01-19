from pydantic import BaseModel
from typing import Optional


class CharacterBase(BaseModel):
    name: Optional[str] = None
    actor_id: Optional[int] = None


class CharacterCreate(CharacterBase):
    pass


class CharacterGet(CharacterBase):
    name: str

    model_config = {"from_attributes": True}


class Character(CharacterBase):
    id: int

    model_config = {"from_attributes": True}


class CharacterResponse(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}
