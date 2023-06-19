from ariadne import convert_kwargs_to_snake_case
from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from app.core.db import engine
from app.modules.users.models import User


@convert_kwargs_to_snake_case
def get_user(obj, info, id: int):
    with Session(engine) as db:
        user = db.get(User, id)
    if not user:
        raise 404
    return user


@convert_kwargs_to_snake_case
def get_users(obj, info, filters: dict):
    query = select(User)

    if filters['search_string']:
        for word in filters['search_string'].split():
            query = query.where(or_(
                User.name.ilike(f'%{word}%'),
                User.email.ilike(f'%{word}%')
            ))

    if filters['offset']:
        query = query.limit(filters['offset'])
    if filters['limit']:
        query = query.limit(filters['limit'])

    with Session(engine) as db:
        users = db.scalars(query).all()

    return users
