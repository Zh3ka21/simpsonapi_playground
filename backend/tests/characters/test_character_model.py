from sqlalchemy.orm import Session
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.models.actor import Actor


def test_character_model(db: Session) -> None:
    actor = Actor(
        first_name="Dan",
        last_name="Castellaneta",
        cast="Main",
    )
    db.add(actor)
    db.commit()
    db.refresh(actor)

    character = Character(
        name="Homer Simpson",
        actor_id=actor.id,
    )

    db.add(character)
    db.commit()
    db.refresh(character)

    assert character.id is not None
    assert character.name == "Homer Simpson"
    assert character.actor_id == actor.id
