from fastapi import FastAPI
from crud_pet import router as pet_router
from crud_tutor import router as tutor_router
from crud_consulta import router as consulta_router

app = FastAPI(title="API Pets")

app.include_router(pet_router, prefix="/pets", tags=["Pets"])
app.include_router(tutor_router, prefix="/tutores", tags=["Tutores"])
app.include_router(consulta_router, prefix="/consultas", tags=["Consultas"])
