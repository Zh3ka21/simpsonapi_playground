# test_db_connection.py
from simpsonapi_playground.core.db import SessionLocal, engine
from simpsonapi_playground.schemas.actor import Base, Actor 

# 1. Verify all tables exist
print("=== Checking database schema ===")
Base.metadata.create_all(bind=engine)
print("Tables loaded:", engine.table_names())

# 2. Open a session
session = SessionLocal()

# 3. Try a simple query
print("=== Testing Actor query ===")
actors = session.query(Actor).limit(5).all()

for actor in actors:
    print(f"{actor.id}: {actor.first_name} {actor.last_name}")

session.close()
