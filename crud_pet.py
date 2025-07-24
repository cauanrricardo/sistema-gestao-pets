from fastapi import APIRouter, HTTPException
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

@router.post("/pet")
async def criar_pet(pet:Pet):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
          "INSERT  INTO pet(id_pet, nome_pet, especie, raca, sexo, data_nasc, peso_atual, id_tutor) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """, 
          ( pet.id_pet,
           pet.nome_pet,
           pet.especie,
           pet.raca,
           pet.sexo,
           pet.data_nasc,
           pet.peso_atual,
           pet.id_tutor) 
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(400, f"Erro ao Cadastrar pet: {e}")
    finally:
        cur.close()
        conn.close()
    return {"msg": "Pet Cadastrado com sucesso"}
    
