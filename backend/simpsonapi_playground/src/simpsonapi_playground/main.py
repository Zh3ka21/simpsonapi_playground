from fastapi import FastAPI

app = FastAPI(title="OpenAPI Playground")

@app.get("/")
def root():
    return {"message": "Hello from OpenAPI Playground"}
