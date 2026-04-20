from sqlalchemy.orm import Session

from simpsonapi_playground.models.actor import Actor
from simpsonapi_playground.models.character import Character


def test_actor_model(db: Session) -> None:
    actor: Actor = Actor(
        first_name="Dan",
        last_name="Castellaneta",
        cast="Homer",
    )

    db.add(actor)
    db.commit()
    db.refresh(actor)

    assert actor.id is not None
