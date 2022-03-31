from flask import Blueprint, request

from resources.bid import BidResource

bid_ = Blueprint('bid', __name__)


@bid_.post('/bid')
def create_bid():
    data = request.get_json()
    return BidResource().post(data=data)

