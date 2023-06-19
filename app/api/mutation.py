from ariadne import ObjectType

from app.modules.users.mutations import create_user

mutation = ObjectType('Mutation')

mutation.set_field('createUser', create_user)
