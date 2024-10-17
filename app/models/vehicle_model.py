from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from app.core.database import Base
from app.models.automaker_model import AutomakerModel


class VehicleModel(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    valor_referencia = Column(Float, nullable=False)
    motorizacao = Column(Integer, nullable=False)
    turbo = Column(Boolean, nullable=False)
    automatico = Column(Boolean, nullable=False)

    montadora_id = Column(Integer, ForeignKey("automaker.id"), nullable=False)

    automaker = relationship("AutomakerModel", back_populates="vehicles")
