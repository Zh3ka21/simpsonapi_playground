from fastapi import FastAPI
from simpsonapi_playground.routers.character import router as character_router
from simpsonapi_playground.routers.actors import router as actor_router
from simpsonapi_playground.routers.episodes import router as episode_router

# import simpsonapi_playground.models

app = FastAPI()

app.include_router(character_router)
app.include_router(actor_router)
app.include_router(episode_router)

app = FastAPI(title="OpenAPI Playground")

app.include_router(character_router)
app.include_router(actor_router)
app.include_router(episode_router)


@app.get("/")
def root():
    return {"message": "Hello from OpenAPI Playground"}
