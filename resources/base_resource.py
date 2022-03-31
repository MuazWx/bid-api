from typing import Union, Type, Tuple, List, Dict

from flask import jsonify

from sqlalchemy.exc import IntegrityError


from exceptions import DataNotFound, FailedToInsert, RequestBodyException
from schemas.bid import BidCrud

from schemas.user import UserCrud
from schemas.product import ProductCrud


class BaseResource:
    def __init__(
            self,
            crud: Union[
                Type[UserCrud],
                Type[ProductCrud],
                Type[BidCrud]
            ]
    ):
        self.crud = crud()

    @staticmethod
    def __check_body(data: any):
        if data is None:
            raise RequestBodyException

    @staticmethod
    def make_response(message: str = None, data: any = None, status: int = 200):
        if message:
            return {'message': message}, status
        else:
            return jsonify(data), status

    def get(self, _id: Union[int, str] = None) -> Tuple[dict, int]:
        try:
            res = self.crud.get(_id)
            if _id:
                return self.make_response(data=self.crud.schema().dump(res))
        except DataNotFound as e:
            return self.make_response(message=str(e), status=404)
        return self.make_response(data=self.crud.schema(many=True).dump(res))

    def post(self, data: Dict[str, Union[int, str]]) -> Tuple[dict, int]:
        try:
            self.__check_body(data)
            res = self.crud.insert(data)
            return self.make_response(data=self.crud.schema().dump(res))
        except RequestBodyException as e:
            return self.make_response(message=str(e), status=400)
        except FailedToInsert as e:
            return self.make_response(message=str(e), status=400)
        except IntegrityError as e:
            return self.make_response(message=str(e), status=400)

    def patch(self, _id: Union[int, str], data: any) -> Tuple[dict, int]:
        try:
            res = self.crud.update(_id, data)
            return self.crud.schema().dump(res), 200
        except DataNotFound as e:
            return self.make_response(message=str(e), status=400)
        except FailedToInsert as e:
            return self.make_response(message=str(e), status=400)
        except IntegrityError as e:
            return self.make_response(message=str(e), status=400)

    def delete(self, _id: Union[int, str]) -> Tuple[dict, int]:
        try:
            res: any = self.crud.delete(_id)
            return self.make_response(data=res, status=200)
        except DataNotFound as e:
            return self.make_response(message=str(e), status=404)


