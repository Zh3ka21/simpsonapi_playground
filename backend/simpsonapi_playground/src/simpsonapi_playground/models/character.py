from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    actor_id = Column(Integer, ForeignKey("actors.id"))

    actor = relationship("Actor", back_populates="characters")
    catchphrases = relationship("Catchphrase", back_populates="character")
    quotes = relationship("Quote", back_populates="character")
