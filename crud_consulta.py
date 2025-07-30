from fastapi import APIRouter, HTTPException
from db import get_connection
from models import Consulta, ConsultaCreate
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Consulta])
async def listar_consultas():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM consulta")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        Consulta(
            id_consulta=row[0],
            id_pet=row[1],
            id_profissional=row[2],
            data=row[3],
            hora=row[4],
            descricao=row[5],
            prescricao=row[6],
            diagnostico=row[7]
        ) for row in rows
    ]

@router.post("/consulta")
async def criar_consulta(consulta: ConsultaCreate):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO consulta (id_consulta, id_pet, id_profissional, data, hora, descricao, prescricao, diagnostico) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (
                consulta.id_consulta,
                consulta.id_pet,
                consulta.id_profissional,
                consulta.data,
                consulta.hora,
                consulta.descricao,
                consulta.prescricao,
                consulta.diagnostico
            )
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(400, f"Erro ao cadastrar consulta: {e}")
    finally:
        cur.close()
        conn.close()
    return {"msg": "Consulta cadastrada com sucesso"}
