
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base


class Catchphrase(Base):
    __tablename__ = "catchphrases"

    id = Column(Integer, primary_key=True)
    phrase = Column(String)
    
    character_id = Column(Integer, ForeignKey("characters.id"))

    character = relationship("Character", backref="catchphrases")
