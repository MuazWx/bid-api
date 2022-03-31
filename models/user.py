from sqlalchemy import Column

from db import db
from models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    username = Column(db.String(80), nullable=False, unique=True)
    password = Column(db.String(255))
    email = Column(db.String(50), nullable=False, unique=True)





