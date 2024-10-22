from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.crud import vehicle_crud
from app.crud import automaker_crud
from app.core.config import templates
from app.schemas import vehicle_schema

router = APIRouter()


@router.get("/veiculos")
def vehicles_list_page(request: Request, db: Session = Depends(get_db)):
    vehicles = vehicle_crud.get_vehicles(db=db)

    return templates.TemplateResponse(
        request=request, name="vehicles_list.html", context={"vehicles": vehicles}
    )


@router.get("/veiculos/criar")
def vehicle_create_page(request: Request, db: Session = Depends(get_db)):
    montadoras = automaker_crud.get_automakers(db)

    return templates.TemplateResponse(
        request=request,
        name="vehicle_create.html",
        context={"montadoras_list": montadoras},
    )


@router.post("/veiculos")
def vehicle_create(
    nome: str = Form(...),
    valor_referencia: float = Form(...),
    motorizacao: float = Form(...),
    turbo: bool = Form(False),
    automatico: bool = Form(False),
    montadora_id: int = Form(...),
    db: Session = Depends(get_db),
):
    try:
        input_vehicle = vehicle_schema.VehicleCreate(
            nome=nome,
            automatico=bool(automatico),
            montadora_id=montadora_id,
            motorizacao=motorizacao,
            turbo=bool(turbo),
            valor_referencia=valor_referencia,
        )

        print(input_vehicle)

        vehicle_crud.create_vehicle(db, input_vehicle)

        return RedirectResponse(url="/veiculos", status_code=303)
    except Exception as e:
        return HTTPException(400, detail=str(e))
