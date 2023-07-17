import enum

from sqlalchemy import Column, Integer, String, Date, Enum

from app.core.models import BaseMixin


class PassportType(enum.Enum):
    Internal = 'INTERNAL'
    External = 'EXTERNAL'


class Passport(BaseMixin):
    __tablename__ = 'passports'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False, unique=True)
    country = Column(String, nullable=False)
    date_of_issue = Column(Date, nullable=False)
    type = Column(Enum(PassportType), nullable=False)




