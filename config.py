class TestConfig:
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "change-this-key-in-the-application-config"
    JWT_SECRET_KEY = "change-this-key-to-something-different-in-the-application-config"


class Config:

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://develop:root123@localhost/newDB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "change-this-key-in-the-application-config"
    JWT_SECRET_KEY = "change-this-key-to-something-different-in-the-application-config"
