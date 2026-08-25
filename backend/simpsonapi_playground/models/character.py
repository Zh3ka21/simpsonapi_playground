import uuid

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base
from sqlalchemy.dialects.postgresql import UUID


class Character(Base):
    """Represents a character from The Simpsons.

    Attributes:
        id: Unique identifier for the character.
        name: Character's name.
        actor_id: Foreign key referencing the actor who voices this character.
        actor: Relationship to the Actor object.
        catchphrases: Relationship to associated Catchphrase objects.
        quotes: Relationship to associated Quote objects.
    """

    __tablename__ = "characters"

    # id = Column(Integer, primary_key=True, index=True)
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )

    name = Column(String)
    actor_id = Column(UUID(as_uuid=True), ForeignKey("actors.id"))

    actor = relationship("Actor", back_populates="characters")
    catchphrases = relationship("Catchphrase", back_populates="character")
    quotes = relationship("Quote", back_populates="character")
