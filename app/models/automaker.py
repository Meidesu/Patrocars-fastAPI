from sqlmodel import Field, SQLModel


class Automaker(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    pais: str
    ano_fundacao: int
