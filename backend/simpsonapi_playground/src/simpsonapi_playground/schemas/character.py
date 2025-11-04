
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base

class Character(Base):
    """
    Represents a fictional character in the Simpsons universe.
    Each character is played by one actor.
    """
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    actor_id = Column(Integer, ForeignKey("actors.id"))

    # Relationships
    actor = relationship("Actor", back_populates="characters")
    catchphrases = relationship("Catchphrase", back_populates="character")
    quotes = relationship("Quote", back_populates="character")

    def __repr__(self):
        return f"<Character(id={self.id}, name='{self.name}')>"

