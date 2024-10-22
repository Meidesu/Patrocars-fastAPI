from sqlalchemy.orm import Session

from app.models import vehicle_model
from app.models.automaker_model import AutomakerModel
from app.models.vehicle_model import VehicleModel
from app.schemas import automaker_schema, vehicle_schema


def create_vehicle(db: Session, vehicle: vehicle_schema.VehicleCreate):
    db_vehicle = VehicleModel(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def get_vehicles(db: Session):
    db_vehicle_base: list[vehicle_model.VehicleModel] = db.query(VehicleModel).all()

    vehicle_response: list[vehicle_schema.VehicleResponse] = []

    for vehicle in db_vehicle_base:
        montadora = (
            db.query(AutomakerModel)
            .filter(AutomakerModel.id == vehicle.montadora_id)
            .first()
        )

        montadora_response = automaker_schema.AutomakerResponse(
            id=montadora.id,
            ano_fundacao=montadora.ano_fundacao,
            nome=montadora.nome,
            pais=montadora.pais,
        )

        vehicle_response.append(
            vehicle_schema.VehicleResponse(
                id=vehicle.id,
                automatico=vehicle.automatico,
                montadora=montadora_response,
                motorizacao=vehicle.motorizacao,
                nome=vehicle.nome,
                turbo=vehicle.turbo,
                valor_referencia=vehicle.valor_referencia,
            )
        )

    return vehicle_response


def get_vehicle(db: Session, vehicle_id: int):
    db_vehicle = db.query(VehicleModel).filter(VehicleModel.id == vehicle_id).first()

    montadora = (
        db.query(AutomakerModel)
        .filter(AutomakerModel.id == db_vehicle.montadora_id)
        .first()
    )

    return vehicle_schema.VehicleResponse(
        id=db_vehicle.id,
        automatico=db_vehicle.automatico,
        montadora=montadora,
        motorizacao=db_vehicle.motorizacao,
        nome=db_vehicle.nome,
        turbo=db_vehicle.turbo,
        valor_referencia=db_vehicle.valor_referencia,
    )


def update_vehicle(
    db: Session, vehicle_id: int, new_vehicle: vehicle_schema.VehicleUpdate
) -> vehicle_schema.VehicleResponse | None:
    old_vehicle = db.query(VehicleModel).filter(VehicleModel.id == vehicle_id).first()

    if old_vehicle:
        for key, value in new_vehicle.dict(exclude_unset=True).items():
            setattr(old_vehicle, key, value)

        db.commit()
        db.refresh(old_vehicle)

        return old_vehicle

    return None


def delete_vehicle(
    db: Session, vehicle_id: int
) -> vehicle_schema.VehicleResponse | None:
    db_vehicle = db.query(VehicleModel).filter(VehicleModel.id == vehicle_id).first()

    if db_vehicle:
        db.delete(db_vehicle)
        db.commit()

        return db_vehicle

    return None
