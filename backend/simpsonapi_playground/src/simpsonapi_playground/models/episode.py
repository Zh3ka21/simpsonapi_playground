from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base

class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    number = Column(Integer)
    season_id = Column(Integer, ForeignKey("seasons.id"))

    season = relationship("Season", back_populates="episodes")
    quotes = relationship("Quote", back_populates="episode")
