from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from app.core.database import Base
from app.models.automaker_model import AutomakerModel


class VehicleModel(Base):
    """
    VehicleModel represents the schema for the 'vehicle' table in the database.
    Attributes:
        id (int): Primary key for the vehicle.
        nome (str): Name of the vehicle.
        valor_referencia (float): Reference value of the vehicle.
        motorizacao (int): Engine capacity of the vehicle.
        turbo (bool): Indicates if the vehicle has a turbo engine.
        automatico (bool): Indicates if the vehicle has an automatic transmission.
        montadora_id (int): Foreign key referencing the automaker.
        automaker (AutomakerModel): Relationship to the AutomakerModel, representing the automaker of the vehicle.
    """

    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    valor_referencia = Column(Float, nullable=False)
    motorizacao = Column(Integer, nullable=False)
    turbo = Column(Boolean, nullable=False)
    automatico = Column(Boolean, nullable=False)

    montadora_id = Column(Integer, ForeignKey("automaker.id"), nullable=False)

    automaker = relationship("AutomakerModel", back_populates="vehicles")
