
from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base

class Quote(Base):
    """
    Represents a spoken line by a character in a specific episode.
    """
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True)
    quote = Column(String)
    date = Column(Date)
    character_id = Column(Integer, ForeignKey("characters.id"))
    episode_id = Column(Integer, ForeignKey("episodes.id"))

    # Relationships
    character = relationship("Character", back_populates="quotes")
    episode = relationship("Episode", back_populates="quotes")

    def __repr__(self):
        return f"<Quote(id={self.id}, quote='{self.quote[:20]}...')>"

