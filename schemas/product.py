from marshmallow_enum import EnumField

from ma import ma
from models.base_model import BasicCrud
from models.enums import ProductType
from models.product import Product


class BaseProductSchema(ma.SQLAlchemyAutoSchema):
    type = EnumField(ProductType, by_value=True)

    class Meta:
        model = Product
        load_instance = True
        include_fk = True


class ProductSchema(BaseProductSchema):
    user = ma.Nested("UserSchema")


class ProductCrud(BasicCrud):
    def __init__(self):
        super(ProductCrud, self).__init__(
            base_schema=BaseProductSchema,
            schema=ProductSchema,
            input_schema=BaseProductSchema,
            model=Product
        )
