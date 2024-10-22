from typing import Optional
from pydantic import BaseModel
from app.schemas import automaker_schema


class VehicleBase(BaseModel):
    nome: str
    valor_referencia: float
    motorizacao: int
    turbo: bool
    automatico: bool
    montadora_id: int


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(VehicleBase):
    id: int


class VehicleResponse(BaseModel):
    id: int
    nome: str
    valor_referencia: float
    motorizacao: int
    turbo: bool
    automatico: bool
    montadora: automaker_schema.AutomakerResponse
