from sqlalchemy import Column, Integer, ForeignKey, Float

from models.base_model import BaseModel


class Bid(BaseModel):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    bid_amount = Column(Float(precision=2), nullable=False)
