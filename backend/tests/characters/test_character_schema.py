from simpsonapi_playground.schemas.actors_schemas import ActorSchema
from simpsonapi_playground.schemas.characters_schemas import CharacterSchema


def test_character_schema_serialization() -> None:
    schema: CharacterSchema = CharacterSchema(
        id=1,
        name="Homer Simpson",
        actor_id=1,
    )

    assert schema.name == "Homer Simpson"
    assert schema.id == 1
