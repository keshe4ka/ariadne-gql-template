from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.db import engine
from app.modules.users.models import User


def create_user(obj, info, data):
    user = User(**data)
    with Session(engine) as db:
        db.add(user)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            return {'error': {'code': 1, 'message': 'email is already exist'}}
        db.refresh(user)
    return {'user': user}
