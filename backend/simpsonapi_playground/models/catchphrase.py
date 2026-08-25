import uuid

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base
from sqlalchemy.dialects.postgresql import UUID


class Catchphrase(Base):
    """Represents a catchphrase associated with a character.

    Attributes:
        id: Unique identifier for the catchphrase.
        phrase: The actual catchphrase text.
        character_id: Foreign key referencing the associated character.
        character: Relationship to the Character object.
    """

    __tablename__ = "catchphrases"

    # id = Column(Integer, primary_key=True, index=True)
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    phrase = Column(String)
    character_id = Column(UUID(as_uuid=True), ForeignKey("characters.id"))

    character = relationship("Character", back_populates="catchphrases")
