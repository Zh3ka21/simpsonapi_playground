from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base

class Catchphrase(Base):
    """
    Famous phrases or lines associated with a particular character.
    """
    __tablename__ = "catchphrases"

    id = Column(Integer, primary_key=True)
    phrase = Column(String)
    character_id = Column(Integer, ForeignKey("characters.id"))

    # Relationships
    character = relationship("Character", back_populates="catchphrases")

    def __repr__(self):
        return f"<Catchphrase(id={self.id}, phrase='{self.phrase}')>"
