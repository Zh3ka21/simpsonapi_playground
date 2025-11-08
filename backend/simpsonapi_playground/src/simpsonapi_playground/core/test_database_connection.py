# test_db_connection.py
from simpsonapi_playground.core.db import Base, SessionLocal, engine
from simpsonapi_playground.models.actor import Actor
from simpsonapi_playground.models.character import Character
from simpsonapi_playground.models.catchphrase import Catchphrase
from simpsonapi_playground.models.episode import Episode
from simpsonapi_playground.models.season import Season
from simpsonapi_playground.models.quote import Quote

from sqlalchemy import inspect

# 1. Verify all tables exist
print("=== Checking database schema ===")
Base.metadata.create_all(bind=engine)
inspector = inspect(engine)
print("Tables loaded:", inspector.get_table_names())

# 2. Open a session
session = SessionLocal()

# 3. Try a simple query
print("=== Testing Actor query ===")
actors = session.query(Actor).limit(5).all()

episodes = session.query(Episode).filter(Episode.title.like('%Bart%')).limit(10).all()

for ep in episodes:
    print(ep.title, ep.season_id, ep.season.average_viewers, ep.quotes, ep.number)

for actor in actors:
    print(f"{actor.id}: {actor.first_name} {actor.last_name}")

session.close()
