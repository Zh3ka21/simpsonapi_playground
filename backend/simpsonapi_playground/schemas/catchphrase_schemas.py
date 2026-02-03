from pydantic import BaseModel
from typing import Optional


class CatchphraseBase(BaseModel):
    phrase: Optional[str] = None
    character_id: Optional[int] = None


class CatchphraseCreate(CatchphraseBase):
    pass


class CatchphraseResponse(CatchphraseBase):
    pass


class CatchphraseSchema(CatchphraseBase):
    id: int

    model_config = {"from_attributes": True}


class PaginatedCatchphrases(BaseModel):
    items: list[CatchphraseSchema]
    total: int
    limit: int
    offset: int
