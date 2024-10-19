from typing import Optional
from pydantic import BaseModel


class AutomakerBase(BaseModel):
    """
    Automaker schema for representing an automaker entity.

    Attributes:
        id (int): Unique identifier for the automaker.
        nome (str): Name of the automaker.
        pais (str): Country where the automaker is based.
        ano_funcao (int): Year the automaker was founded.
    """

    nome: str
    pais: str
    ano_fundacao: int


class AutomakerCreate(AutomakerBase):
    pass


class AutomakerGet(AutomakerBase):
    id: int


class AutomakerUpdate(BaseModel):
    nome: Optional[str]
    pais: Optional[str]
    ano_fundacao: Optional[int]
