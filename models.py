from pydantic import BaseModel
from datetime import date

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
    nome_pet: str
    especie: str
    raca: str
    sexo: str
    data_nasc: date
    peso_atual: float
    id_tutor: int