from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class CatchphraseBase(BaseModel):
    phrase: Optional[str] = None
    character_id: Optional[UUID] = None


class CatchphraseCreate(CatchphraseBase):
    pass


class CatchphraseResponse(CatchphraseBase):
    id: UUID

    model_config = {"from_attributes": True}


class PaginatedCatchphrases(BaseModel):
    items: list[CatchphraseResponse]
    total: int
    limit: int
    offset: int
