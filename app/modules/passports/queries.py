from operator import or_

from ariadne import convert_kwargs_to_snake_case
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.db import engine
from app.modules.passports.models import Passport


@convert_kwargs_to_snake_case
def get_passport(obj, info, number: int):
    with Session(engine) as db:
        passport = db.scalar(select(Passport).filter_by(number=number))
    if not passport:
        raise 404
    return passport


@convert_kwargs_to_snake_case
def get_passports(obj, info, filters: dict):
    query = select(Passport)

    if filters['search_string']:
        for word in filters['search_string'].split():
            query = query.where(or_(
                Passport.country.ilike(f'%{word}%'),
                Passport.type.ilike(f'%{word}%')
            ))

    if filters['offset']:
        query = query.limit(filters['offset'])
    if filters['limit']:
        query = query.limit(filters['limit'])

    with Session(engine) as db:
        passports = db.scalars(query).all()

    return passports
