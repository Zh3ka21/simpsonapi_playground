from simpsonapi_playground.schemas.actors_schemas import ActorSchema
from simpsonapi_playground.schemas.characters_schemas import CharacterSchema
from uuid import UUID

TEST_ID = UUID("22222222-2222-2222-2222-222222222222")
ACTOR_ID = UUID("11111111-1111-1111-1111-111111111111")


def test_character_schema_serialization() -> None:
    schema: CharacterSchema = CharacterSchema(
        id=TEST_ID,
        name="Homer Simpson",
        actor_id=ACTOR_ID,
    )

    assert schema.name == "Homer Simpson"
    assert schema.id == TEST_ID
