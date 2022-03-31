from flask import Blueprint, request

from resources.user import UserResource

user_ = Blueprint('user', __name__)


@user_.get('/user/<int:user_id>')
def get_user(user_id: int):
    return UserResource().get(user_id=user_id)


@user_.post('/register')
def create_user():
    data = request.get_json()
    return UserResource().post(data=data)


@user_.patch('/user')
def update_user():
    data = request.get_json()
    return UserResource().patch(data=data)


@user_.delete('/user')
def delete_user():
    return UserResource().delete()


@user_.post('/login')
def login_user():
    data = request.get_json()
    return UserResource().login(data)
