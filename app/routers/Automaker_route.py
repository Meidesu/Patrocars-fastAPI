from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.core.config import templates
from app.core.database import get_db
from app.crud import automaker_crud
from app.models.vehicle_model import VehicleModel
from app.schemas import automaker_schema

router = APIRouter()


@router.post("/automakers")
def create_automaker(
    _input: Annotated[automaker_schema.AutomakerCreate, Form()],
    db: Session = Depends(get_db),
):
    """
    Create a new automaker entry in the database.

    Args:
        automaker (automaker_schema.AutomakerCreate): The automaker data to be created.
        db (Session, optional): The database session dependency.

    Returns:
        The created automaker entry.
    """
    try:
        new_automaker = automaker_schema.AutomakerCreate(
            nome=_input.nome, pais=_input.pais, ano_fundacao=_input.ano_fundacao
        )

        automaker_crud.create_automaker(db, new_automaker)

        return RedirectResponse(url="/automakers", status_code=303)

    except Exception as e:
        return HTTPException(400, detail=str(e))


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


@router.get("/automakers/create")
def automaker_create_page(request: Request):
    return templates.TemplateResponse(name="automaker_create.html", request=request)


@router.get("/automakers/edit/{automaker_id}")
def automaker_edit_page(
    automaker_id: int, request: Request, db: Session = Depends(get_db)
):
    automaker = automaker_crud.get_automaker(db=db, automaker_id=automaker_id)

    return templates.TemplateResponse(
        request=request, name="automaker_update.html", context={"automaker": automaker}
    )


@router.post("/automakers/{automaker_id}")
def update_automaker(
    automaker_id: int,
    _input: Annotated[automaker_schema.AutomakerUpdate, Form()],
    db: Session = Depends(get_db),
):
    new_automaker = automaker_schema.AutomakerUpdate(
        nome=_input.nome, pais=_input.pais, ano_fundacao=_input.ano_fundacao
    )

    updated_automaker = automaker_crud.update_automaker(
        automaker_id=automaker_id, db=db, automaker_update=new_automaker
    )

    if not updated_automaker:
        return HTTPException(400, detail="Falha ao atualizar montadora")

    return RedirectResponse(url="/automakers", status_code=303)


@router.post("/automakers/delete/{automaker_id}")
def delete_automaker(automaker_id: int, db: Session = Depends(get_db)):
    automaker = automaker_crud.delete_automaker(db=db, automaker_id=automaker_id)

    if not automaker:
        return HTTPException(400, detail="Falha ao deletar montadora")

    return RedirectResponse(url="/automakers", status_code=303)
