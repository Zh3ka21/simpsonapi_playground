
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    cast = Column(String)

    characters = relationship("Character", back_populates="actor")
