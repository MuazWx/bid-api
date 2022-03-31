from flask_jwt_extended import jwt_required, get_jwt_identity

from resources.base_resource import BaseResource
from schemas.bid import BidCrud
from schemas.product import ProductCrud, ProductSchema
from utils.error_handling import LOG


class BidResource(BaseResource):
    def __init__(self):
        super(BidResource, self).__init__(crud=BidCrud)

    @jwt_required()
    def post(self, data):
        data['user_id'] = get_jwt_identity()
        product = ProductCrud().find_by_id(data['product_id'])
        if product.user_id == data['user_id']:
            return {'msg': 'You can not bid for your own product!'}
        if product.highest_bid+product.bid_increase < (data['bid_amount']):
            product = ProductSchema().dump(product)
            product.pop('user')
            LOG(product)
            product['highest_bid'] = data['bid_amount']
            ProductCrud().update(product['id'], product)

            return super(BidResource, self).post(data)

        return {'msg': 'Data not found.'}

