from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base


class Actor(Base):
    """Represents a voice actor or actor in The Simpsons.

    Attributes:
        id: Unique identifier for the actor.
        first_name: Actor's first name.
        last_name: Actor's last name.
        cast: Cast/role name or notes.
        characters: Relationship to Character objects voiced by this actor.
    """

    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    cast = Column(String)

    characters = relationship("Character", back_populates="actor")
