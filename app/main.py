from typing import Union

from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import SQLModel

from app.persistence.automaker_repositoy import AutomakerRepository
from app.persistence.utils import get_engine
from app.schemas.montadora_schema import Automaker
from app.models.automaker import Automaker

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.add_middleware(GZipMiddleware)

templates = Jinja2Templates(directory="app/templates")

SQLModel.metadata.create_all(get_engine())

# montadoras = [
#     Automaker(id=1, nome="Chevrolet", ano_fundacao=1911, pais="Estados Unidos"),
#     Automaker(id=2, nome="Fiat", ano_fundacao=1899, pais="Itália"),
#     Automaker(id=3, nome="Ford", ano_fundacao=1903, pais="Estados Unidos"),
#     Automaker(id=4, nome="Volkswagen", ano_fundacao=1937, pais="Alemanha"),
#     Automaker(id=5, nome="Renault", ano_fundacao=1899, pais="França"),
# ]

repository = AutomakerRepository()


@app.get("/")
def home(request: Request):
    """
    Handles the HTTP request for the home page and returns a TemplateResponse.

    Args:
        request: The HTTP request object.

    Returns:
        TemplateResponse: The response object containing the rendered home page template.
    """
    return templates.TemplateResponse(name="home.html", request=request)


@app.get("/automakers")
def get_all_automaker(request: Request):
    """
    Devolve uma lista de todas as montadoras.

    retorna:
        list[Automaker]: A list containing all automaker objects.
    """

    automakers = repository.get_all()

    return templates.TemplateResponse(
        request=request,
        name="automakers_list.html",
        context={"montadoras": automakers},
    )


@app.get("/automakers/{id}")
def read_item(automaker_id: int, q: Union[str, None] = None):
    """
    Retrieve an item by its ID and an optional query parameter.

    Args:
        id (int): The ID of the item to retrieve.
        q (Union[str, None], optional): An optional query parameter. Defaults to None.

    Returns:
        dict: A dictionary containing the item ID and the query parameter.
    """
    return {"id": automaker_id, "q": q}
