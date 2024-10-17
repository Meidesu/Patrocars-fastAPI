from fastapi.templating import Jinja2Templates
from app.main import templates


def get_templates() -> Jinja2Templates:
    return templates
