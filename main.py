from fastapi import FastAPI
from app import person, gplay


app = FastAPI()
app.include_router(person.router)
app.include_router(gplay.router, prefix="/api/v1/gplay", tags=["Google Play Scrapper"])

@app.get("/ping")
def ping():
    return {
        "message": "pong"
    }
