from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class Pet(BaseModel):
    id_pet: int
    nome_pet: str
    especie: str
    raca: str
    sexo: str
    data_nasc: date
    peso_atual: float
    id_tutor: int

class PetUpdate(BaseModel):
    nome_pet: Optional[str] = None
    especie: Optional[str] = None
    raca: Optional[str] = None
    sexo: Optional[str] = None
    data_nasc: Optional[date] = None
    peso_atual: Optional[float] = None
    id_tutor: Optional[int] = None


from pydantic import BaseModel
from typing import Optional

class Tutor(BaseModel):
    id_tutor: int
    nome: str
    cpf: str
    telefone: str
    email: str
    cep: str
    bairro: str
    cidade: str
    numero: int
    rua: str

class TutorUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    cep: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    numero: Optional[int] = None
    rua: Optional[str] = None

class Consulta(BaseModel):
    id_consulta: int
    id_pet: int
    id_profissional: int
    data: date
    hora: time
    descricao: str
    prescricao: str
    diagnostico: str

class ConsultaCreate(BaseModel):
    id_consulta: int
    id_pet: int
    id_profissional: int
    data: date
    hora: time
    descricao: str
    prescricao: str
    diagnostico: str