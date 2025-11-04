from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base

class Actor(Base):
    """
    Represents a real-world actor who voices or portrays characters.
    One actor can voice multiple characters.
    """
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    cast = Column(String)

    # Relationships
    characters = relationship("Character", back_populates="actor")

    def __repr__(self):
        return f"<Actor(id={self.id}, name='{self.first_name} {self.last_name}')>"

