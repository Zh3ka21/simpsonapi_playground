from simpsonapi_playground.schemas.actors_schemas import ActorSchema
from uuid import UUID

TEST_ID = UUID("11111111-1111-1111-1111-111111111111")


def test_actor_schema_serialization() -> None:
    schema: ActorSchema = ActorSchema(
        id=TEST_ID,
        first_name="Dan",
        last_name="Castellaneta",
        cast="Main",
    )

    assert schema.first_name == "Dan"
    assert schema.id == TEST_ID
