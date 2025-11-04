from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True)
    quote = Column(String)
    date = Column(Date)
    character_id = Column(Integer, ForeignKey("characters.id"))
    episode_id = Column(Integer, ForeignKey("episodes.id"))

    character = relationship("Character", back_populates="quotes")
    episode = relationship("Episode", back_populates="quotes")

