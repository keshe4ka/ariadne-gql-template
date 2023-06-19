from sqlalchemy import Column, String, Integer

from app.core.models import BaseMixin


class User(BaseMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
