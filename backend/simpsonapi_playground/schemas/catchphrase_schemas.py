from pydantic import BaseModel
from typing import Optional


class CatchphraseBase(BaseModel):
    phrase: Optional[str] = None
    character_id: Optional[int] = None


class CatchphraseCreate(CatchphraseBase):
    pass


class CatchphraseResponse(CatchphraseBase):
    id: int

    model_config = {"from_attributes": True}


class PaginatedCatchphrases(BaseModel):
    items: list[CatchphraseResponse]
    total: int
    limit: int
    offset: int
