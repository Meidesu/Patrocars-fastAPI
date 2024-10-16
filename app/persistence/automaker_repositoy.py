from sqlmodel import Session, select
from app.models.automaker import Automaker
from app.persistence.utils import get_engine


class AutomakerRepository:
    def __init__(self):
        self.session = Session(get_engine())

    def get_all(self):
        sttm = select(Automaker).order_by(Automaker.nome)
        result = self.session.exec(sttm).all()
        return result
