from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles


from app.routers import automaker_route
from app.routers import vehicle_route

from app.core.config import templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.add_middleware(GZipMiddleware)

app.include_router(automaker_route.router)
app.include_router(vehicle_route.router)


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


# @app.get("/automakers")
# def get_all_automaker(request: Request):
#     """
#     Devolve uma lista de todas as montadoras.

#     retorna:
#         list[Automaker]: A list containing all automaker objects.
#     """

#     automakers = repository.get_all()

#     return templates.TemplateResponse(
#         request=request,
#         name="automakers_list.html",
#         context={"montadoras": automakers},
#     )


# @app.get("/automakers/{id}")
# def read_item(automaker_id: int, q: Union[str, None] = None):
#     """
#     Retrieve an item by its ID and an optional query parameter.

#     Args:
#         id (int): The ID of the item to retrieve.
#         q (Union[str, None], optional): An optional query parameter. Defaults to None.

#     Returns:
#         dict: A dictionary containing the item ID and the query parameter.
#     """
#     return {"id": automaker_id, "q": q}
