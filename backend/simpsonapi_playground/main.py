from fastapi import FastAPI
from simpsonapi_playground.routers.character import router as character_router
from simpsonapi_playground.routers.actors import router as actor_router
from simpsonapi_playground.routers.episodes import router as episode_router
from simpsonapi_playground.routers.catchphrases import router as catchphrase_router
from simpsonapi_playground.routers.quotes import router as quotes_router
from simpsonapi_playground.routers.seasons import router as seasons_router

# import simpsonapi_playground.models

app = FastAPI()

app.include_router(character_router)
app.include_router(actor_router)
app.include_router(episode_router)
app.include_router(catchphrase_router)
app.include_router(quotes_router)
app.include_router(seasons_router)

app = FastAPI(title="OpenAPI Playground")

app.include_router(character_router)
app.include_router(actor_router)
app.include_router(episode_router)
app.include_router(catchphrase_router)
app.include_router(quotes_router)
app.include_router(seasons_router)


@app.get("/")
def root():
    return {"message": "Hello from OpenAPI Playground"}
