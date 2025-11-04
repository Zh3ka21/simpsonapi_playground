
from sqlalchemy import Column, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base


class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    year_start = Column(Integer)
    year_end = Column(Integer)
    season_premiere = Column(Date)
    season_finale = Column(Date)
    average_viewers = Column(Integer)
    most_watched_episode_id = Column(Integer, ForeignKey("episodes.id"))
    most_watched_episode_viewers = Column(Integer)

    most_watched_episode = relationship("Episode", foreign_keys=[most_watched_episode_id])
    episodes = relationship("Episode", back_populates="season")
