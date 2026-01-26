from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base


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

    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String)
    episode_id = Column(Integer, ForeignKey("episodes.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))

    episode = relationship("Episode", back_populates="quotes")
    character = relationship("Character", back_populates="quotes")
