from ariadne import ObjectType

from app.modules.passports.queries import get_passport, get_passports
from app.modules.users.queries import get_user, get_users

query = ObjectType('Query')

query.set_field('getUser', get_user)
query.set_field('getUsers', get_users)
query.set_field('getPassport', get_passport)
query.set_field('getPassports', get_passports)


