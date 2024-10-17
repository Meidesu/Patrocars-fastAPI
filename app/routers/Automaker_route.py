from typing import List

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud import automaker_crud
from app.models.vehicle_model import VehicleModel
from app.schemas import automaker_schema
from app.core.config import templates

router = APIRouter()


@router.post("/automakers", response_model=automaker_schema.AutomakerCreate)
def create_automaker(
    automaker: automaker_schema.AutomakerCreate, db: Session = Depends(get_db)
):
    """
    Create a new automaker entry in the database.

    Args:
        automaker (automaker_schema.AutomakerCreate): The automaker data to be created.
        db (Session, optional): The database session dependency.

    Returns:
        The created automaker entry.
    """
    return automaker_crud.create_automaker(db, automaker)


@router.get("/automakers")
def get_automakers(request: Request, db: Session = Depends(get_db)):
    """
    Fetches a list of automakers from the database.

    Args:
        db (Session): Database session dependency.

    Returns:
        List[Automaker]: A list of automaker objects retrieved from the database.
    """
    automakers = automaker_crud.get_automakers(db)

    return templates.TemplateResponse(
        request=request,
        name="automakers_list.html",
        context={"montadoras": automakers},
    )
