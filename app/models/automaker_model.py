from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship


class AutomakerModel(Base):
    __tablename__ = "automaker"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    pais = Column(String)
    ano_fundacao = Column(Integer)

    vehicles = relationship("VehicleModel", back_populates="automaker")
