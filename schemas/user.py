from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

from exceptions import InvalidCredentials
from ma import ma
from models.base_model import BasicCrud

from models.user import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        load_only = ('password',)


class BaseUserSchema:
    pass


class UserCrud(BasicCrud):
    def __init__(self):
        super(UserCrud, self).__init__(
            base_schema=UserSchema,
            schema=UserSchema,
            input_schema=UserSchema,
            model=User
        )

    def find_by_username(self, username):
        return self.db.query(User).filter_by(username=username).first()

    def login(self, username, password):
        user = self.find_by_username(username)
        if user and check_password_hash(pwhash=user.password, password=password):
            return user
        raise InvalidCredentials('Wrong email or password')



