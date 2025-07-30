from fastapi import APIRouter, HTTPException
from db import get_connection
from models import Tutor, TutorUpdate
from typing import List

router = APIRouter()

@router.get("/tutores", response_model=List[Tutor])
async def listar_tutores():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tutor")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        Tutor(
            id_tutor=row[0],
            nome=row[1],
            cpf=row[2],
            telefone=row[3],
            email=row[4],
            cep=row[5],
            bairro=row[6],
            cidade=row[7],
            numero=row[8],
            rua=row[9]
        ) for row in rows
    ]

@router.post("/tutor")
async def criar_tutor(tutor: Tutor):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO tutor (id_tutor, nome, cpf, telefone, email, cep, bairro, cidade, numero, rua) " +
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                tutor.id_tutor, tutor.nome, tutor.cpf, tutor.telefone, tutor.email,
                tutor.cep, tutor.bairro, tutor.cidade, tutor.numero, tutor.rua
            )
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(400, f"Erro ao criar tutor: {e}")
    finally:
        cur.close()
        conn.close()
    return {"msg": "Tutor criado com sucesso"}

@router.patch("/tutor/{id_tutor}")
async def atualizar_tutor(id_tutor: int, tutor: TutorUpdate):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_tutor FROM tutor WHERE id_tutor = %s", (id_tutor,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(404, "Tutor não encontrado")

    fields = []
    values = []
    for campo, valor in tutor.dict(exclude_unset=True).items():
        fields.append(f"{campo} = %s")
        values.append(valor)

    if not fields:
        raise HTTPException(400, "Nenhum dado fornecido para atualização")

    values.append(id_tutor)
    try:
        cur.execute(
            f"UPDATE tutor SET {', '.join(fields)} WHERE id_tutor = %s",
            values
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(400, f"Erro ao atualizar tutor: {e}")
    finally:
        cur.close()
        conn.close()

    return {"msg": "Tutor atualizado com sucesso"}

@router.delete("/tutor/{id_tutor}")
async def deletar_tutor(id_tutor: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_tutor FROM tutor WHERE id_tutor = %s", (id_tutor,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(404, "Tutor não encontrado")

    try:
        cur.execute("DELETE FROM tutor WHERE id_tutor = %s", (id_tutor,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(400, f"Erro ao deletar tutor: {e}")
    finally:
        cur.close()
        conn.close()
    return {"msg": "Tutor removido com sucesso"}
