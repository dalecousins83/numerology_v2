from fastapi import FastAPI
from api import api_router

app = FastAPI(title="Numerology Service")

# include routes from api/__init__.py
app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Numerology API is running"}
