from models.base_model import BasicCrud
from models.bid import Bid
from ma import ma


class BidSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bid
        load_instance = True
        include_fk = True


class BidCrud(BasicCrud):
    def __init__(self):
        super(BidCrud, self).__init__(
            base_schema=BidSchema,
            schema=BidSchema,
            input_schema=BidSchema,
            model=Bid
        )
