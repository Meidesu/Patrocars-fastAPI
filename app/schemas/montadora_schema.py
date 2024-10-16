from pydantic import BaseModel


class Automaker(BaseModel):
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
