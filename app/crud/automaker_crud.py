from sqlalchemy.orm import Session
from app.schemas.automaker_schema import AutomakerCreate
from app.models.automaker_model import AutomakerModel


def create_automaker(db: Session, automaker: AutomakerCreate):
    db_automaker = AutomakerModel(**automaker.dict())
    db.add(db_automaker)
    db.commit()
    db.refresh(db_automaker)
    return db_automaker


def get_automakers(db: Session):
    return db.query(AutomakerModel).all()
