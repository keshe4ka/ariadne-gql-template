from ariadne import ObjectType

from app.modules.users.queries import get_user, get_users

query = ObjectType('Query')

query.set_field('getUser', get_user)
query.set_field('getUsers', get_users)


