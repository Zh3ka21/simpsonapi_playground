import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base
from sqlalchemy.dialects.postgresql import UUID


class Quote(Base):
    """Represents a quote from a Simpsons episode.

    Attributes:
        id: Unique identifier for the quote.
        quote: The actual quote text.
        episode_id: Foreign key referencing the episode where the quote appears.
        character_id: Foreign key referencing the character who said the quote.
        episode: Relationship to the Episode object.
        character: Relationship to the Character object.
    """

    __tablename__ = "quotes"

    __table_args__ = (
        UniqueConstraint("quote", "episode_id", "character_id", name="uq_quote"),
    )

    # id = Column(Integer, primary_key=True, index=True)
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )

    quote = Column(String)
    episode_id = Column(UUID(as_uuid=True), ForeignKey("episodes.id"))
    character_id = Column(UUID(as_uuid=True), ForeignKey("characters.id"))
    episode = relationship("Episode", back_populates="quotes")
    character = relationship("Character", back_populates="quotes")
