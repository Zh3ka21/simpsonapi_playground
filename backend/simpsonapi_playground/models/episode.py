from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base


class Episode(Base):
    """Represents an episode of The Simpsons.

    Attributes:
        id: Unique identifier for the episode.
        title: Episode title.
        number: Episode number within the series.
        season_id: Foreign key referencing the season this episode belongs to.
        season: Relationship to the Season object.
        quotes: Relationship to associated Quote objects.
    """

    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    number = Column(Integer)
    season_id = Column(Integer, ForeignKey("seasons.id"))

    season = relationship("Season", back_populates="episodes")
    quotes = relationship("Quote", back_populates="episode")
