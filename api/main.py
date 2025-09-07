from fastapi import FastAPI
from fastapi import APIRouter
from .routes import numerology, users

app = FastAPI(title="Numerology Service")

# Define router here
api_router = APIRouter()
api_router.include_router(numerology.router, prefix="/numerology", tags=["numerology"])
api_router.include_router(users.router, prefix="/users", tags=["users"])

# Mount router
app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Numerology API is running"}
