from fastapi import FastAPI
from simpsonapi_playground.routers.character import router as character_router

# import simpsonapi_playground.models

app = FastAPI()

# Include the router here
app.include_router(character_router)

app = FastAPI(title="OpenAPI Playground")

app.include_router(character_router)


@app.get("/")
def root():
    return {"message": "Hello from OpenAPI Playground"}
