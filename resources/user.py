from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash


from resources.base_resource import BaseResource
from schemas.user import UserCrud


class UserResource(BaseResource):
    def __init__(self):
        super(UserResource, self).__init__(crud=UserCrud)

    def post(self, data):
        data['password'] = generate_password_hash(data['password'])
        return super().post(data)

    @staticmethod
    def login(data):
        username = data['username']
        password = data['password']
        user = UserCrud().login(username, password)
        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)
        return {"access_token": access_token, "refresh_token": refresh_token}

    @jwt_required()
    def delete(self):
        _id = get_jwt_identity()
        return super().delete(_id)

    @jwt_required()
    def patch(self, data: any):
        _id = get_jwt_identity()
        return super().patch(_id, data)
