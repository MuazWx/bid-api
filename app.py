from flask import Flask
from flask_jwt_extended import JWTManager

from db import db
from ma import ma

from routes.user import user_
from routes.product import product_
from routes.bid import bid_

app = Flask(__name__)

jwt = JWTManager(app)
app.config.from_object("config.Config")
db.init_app(app)
ma.init_app(app)


def create_tables():
    with app.app_context():
        db.create_all()


app.register_blueprint(user_, url_prefix='/api/')
app.register_blueprint(product_, url_prefix='/api/')
app.register_blueprint(bid_, url_prefix='/api/')
create_tables()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
