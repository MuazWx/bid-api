from datetime import datetime
from typing import Type, Union, List

from sqlalchemy import Column, Integer, DateTime

from db import db
from exceptions import DataNotFound, FailedToInsert
from ma import ma


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class BasicCrud:
    def __init__(
            self,
            base_schema: ma.SQLAlchemyAutoSchema,
            schema: ma.SQLAlchemyAutoSchema,
            input_schema: ma.SQLAlchemyAutoSchema,
            model: Type[BaseModel]
    ):
        self.db = db.session
        self.base_schema = base_schema
        self.schema = schema
        self.input_schema = input_schema
        self.model = model
        self.base_query = self.db.query(self.model)

    def find_by_id(self, _id: Union[int, str]) -> BaseModel:
        res = self.base_query.filter_by(id=_id).first()
        if res:
            return res
        raise DataNotFound('Data not found')

    def find_all(self) -> List[BaseModel]:
        return self.base_query.all()

    def get(self, _id: int = None) -> Union[BaseModel, List[BaseModel], None]:
        if _id:
            res = self.find_by_id(_id)
            if res:
                return res
            raise DataNotFound('Data not found')
        else:
            return self.find_all()

    def insert(self, data: any) -> BaseModel:
        try:
            db_data: BaseModel = self.input_schema().load(data)
        except Exception as e:
            raise FailedToInsert(str(e))
        return self.do_upsert(db_data=db_data)

    def update(self, _id: int, data: any) -> BaseModel:
        db_data: Union[BaseModel, None] = self.find_by_id(_id)
        if db_data:
            data['updated_at'] = str(datetime.now())
            updated_data: Union[BaseModel, None] = self.input_schema().load(data, instance=db_data, partial=True)
            return self.do_upsert(db_data=updated_data)
        else:
            raise DataNotFound('Data not found')

    def delete(self, _id: int) -> bool:
        db_data: Union[BaseModel, None] = self.find_by_id(_id)
        if db_data:
            self.db.delete(db_data)
            self.db.commit()
            return True
        else:
            raise DataNotFound('Data not found')

    def do_upsert(self, db_data: BaseModel):
        db_data.updated_at = datetime.utcnow()
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        return db_data
