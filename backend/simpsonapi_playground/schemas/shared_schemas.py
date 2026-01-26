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
