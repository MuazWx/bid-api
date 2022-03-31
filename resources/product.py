from flask_jwt_extended import jwt_required, get_jwt_identity

from exceptions import InvalidCredentials
from resources.base_resource import BaseResource
from schemas.product import ProductCrud


class ProductResource(BaseResource):
    def __init__(self):
        super(ProductResource, self).__init__(crud=ProductCrud)

    @jwt_required()
    def post(self, data):
        data['user_id'] = get_jwt_identity()
        return super().post(data)

    @jwt_required()
    def delete(self, _id):
        user_id = get_jwt_identity()
        product = ProductCrud().find_by_id(_id)
        if product.user_id == user_id:
            return super().delete(_id)
        raise InvalidCredentials('InvalidCredentials')
