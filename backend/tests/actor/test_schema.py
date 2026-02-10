from simpsonapi_playground.schemas.actors_schemas import ActorSchema


def test_actor_schema_serialization() -> None:
    schema: ActorSchema = ActorSchema(
        id=1,
        first_name="Dan",
        last_name="Castellaneta",
        cast="Homer",
    )

    assert schema.first_name == "Dan"
    assert schema.id == 1
