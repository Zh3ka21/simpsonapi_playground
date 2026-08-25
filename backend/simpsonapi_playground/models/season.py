import uuid

from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base
from sqlalchemy.dialects.postgresql import UUID


class Season(Base):
    """Represents a season of The Simpsons.

    Attributes:
        id: Unique identifier for the season.
        number: Season number.
        year_start: Year the season started airing.
        year_end: Year the season ended airing.
        season_premiere: Date of the season premiere.
        season_finale: Date of the season finale.
        average_viewers: Average number of viewers for the season.
        most_watched_episode_id: Episode ID of the most watched episode in this season.
        most_watched_episode_viewers: Number of viewers for the most watched episode.
        episodes: Relationship to Episode objects in this season.
    """

    __tablename__ = "seasons"

    # id = Column(Integer, primary_key=True, index=True)
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )

    number = Column(Integer)
    year_start = Column(Integer)
    year_end = Column(Integer)
    season_premiere = Column(Date)
    season_finale = Column(Date)
    average_viewers = Column(Integer)
    # most_watched_episode_id = Column(UUID(as_uuid=True), ForeignKey("episodes.id"))
    most_watched_episode_viewers = Column(Integer)

    # episodes = relationship("Episode", back_populates="season")
    most_watched_episode_id = Column(
        UUID(as_uuid=True),
        ForeignKey("episodes.id"),
    )

    episodes = relationship(
        "Episode",
        back_populates="season",
        foreign_keys="Episode.season_id",
    )

    most_watched_episode = relationship(
        "Episode",
        foreign_keys=[most_watched_episode_id],
    )
