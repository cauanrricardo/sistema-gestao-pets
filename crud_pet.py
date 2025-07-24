from fastapi import APIRouter
from db import get_connection
from models import Pet
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Pet])
async def listar_pets():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pet")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return [
        Pet(
            id_pet=row[0],
            nome_pet=row[1],
            especie=row[2],
            raca=row[3],
            sexo=row[4],
            data_nasc=row[5],
            peso_atual=row[6],
            id_tutor=row[7]
        ) for row in rows
    ]
