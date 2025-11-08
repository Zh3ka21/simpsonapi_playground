
from sqlalchemy import Column, Date, Integer
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base


class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    year_start = Column(Integer)
    year_end = Column(Integer)
    season_premiere = Column(Date)
    season_finale = Column(Date)
    average_viewers = Column(Integer)
    most_watched_episode_id = Column(Integer)
    most_watched_episode_viewers = Column(Integer)

    episodes = relationship("Episode", back_populates="season")

