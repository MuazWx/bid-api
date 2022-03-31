from sqlalchemy import Column, Integer, ForeignKey, Enum, Float, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.enums import ProductType


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(80), nullable=False)
    starting_price = Column(Float(precision=2), nullable=False, default=0)
    highest_bid = Column(Float(precision=2), nullable=False, default=0)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', foreign_keys=user_id)
    type = Column(Enum(ProductType), nullable=False)
    bid_increase = Column(Integer, nullable=False, default=1)
