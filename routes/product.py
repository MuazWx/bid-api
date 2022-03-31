from flask import Blueprint, request

from resources.product import ProductResource

product_ = Blueprint('product', __name__)


@product_.post('/product')
def create_product():
    data = request.get_json()
    return ProductResource().post(data=data)


@product_.get('/product/<int:product_id>')
def get_product(product_id: int):
    return ProductResource().get(product_id)


@product_.delete('/product/<int: product_id>')
def delete_product(product_id: int):
    return ProductResource().delete(product_id)
