from fastapi import FastAPI
from crud_pet import router as pet_router

app = FastAPI(title="API Pets")

app.include_router(pet_router, prefix="/pets", tags=["Pets"])
