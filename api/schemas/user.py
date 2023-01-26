from api import ma
from api.models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = UserModel
       exclude = ("password_hash",) # Исключить поля

# одиночная
user_schema = UserSchema()
# множественная
users_schema = UserSchema(many=True)
