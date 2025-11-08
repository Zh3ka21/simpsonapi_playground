from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String)
    episode_id = Column(Integer, ForeignKey("episodes.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))

    episode = relationship("Episode", back_populates="quotes")
    character = relationship("Character", back_populates="quotes")
