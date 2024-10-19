from sqlalchemy.orm import Session
from app.schemas.automaker_schema import AutomakerCreate, AutomakerUpdate
from app.models.automaker_model import AutomakerModel


def create_automaker(db: Session, automaker: AutomakerCreate):
    db_automaker = AutomakerModel(**automaker.dict())
    db.add(db_automaker)
    db.commit()
    db.refresh(db_automaker)
    return db_automaker


def get_automakers(db: Session):
    return db.query(AutomakerModel).all()


def get_automaker(db: Session, automaker_id: int):
    return db.query(AutomakerModel).filter(AutomakerModel.id == automaker_id).first()


def update_automaker(db: Session, automaker_id: int, automaker_update: AutomakerUpdate):
    db_montadora = (
        db.query(AutomakerModel).filter(AutomakerModel.id == automaker_id).first()
    )

    if db_montadora:
        for key, value in automaker_update.dict(exclude_unset=True).items():
            setattr(db_montadora, key, value)
        db.commit()
        db.refresh(db_montadora)

        return db_montadora

    return None
