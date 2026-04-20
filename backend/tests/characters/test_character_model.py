from sqlalchemy.orm import Session
from simpsonapi_playground.models.character import Character


def test_character_model(db: Session) -> None:
    character: Character = Character(
        name="Homer Simpson",
        actor_id=1,
    )

    db.add(character)
    db.commit()
    db.refresh(character)

    assert character.id is not None
    assert character.name == "Homer Simpson"
    assert character.actor_id == 1
