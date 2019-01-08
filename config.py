# default config
import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\x06}\x90\x1f\x87\x9e\xc9\xda\x1de;:8\xf6wP\xa8\xc1e\xa2{\xe5SI'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
