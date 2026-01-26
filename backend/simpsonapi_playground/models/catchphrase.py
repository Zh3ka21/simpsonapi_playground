from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from simpsonapi_playground.core.db import Base


class Catchphrase(Base):
    """Represents a catchphrase associated with a character.

    Attributes:
        id: Unique identifier for the catchphrase.
        phrase: The actual catchphrase text.
        character_id: Foreign key referencing the associated character.
        character: Relationship to the Character object.
    """

    __tablename__ = "catchphrases"

    id = Column(Integer, primary_key=True, index=True)
    phrase = Column(String)
    character_id = Column(Integer, ForeignKey("characters.id"))

    character = relationship("Character", back_populates="catchphrases")
