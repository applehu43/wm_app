import os
from flask_sqlalchemy import SQLAlchemy

databases = {
    'production':{
    },
    'development': {
        'ENGINE': 'mysql',
        'NAME': 'db_spring',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST':'',
        'PORT':'',
        'OPTIONS':{
            'autocommit': True,
        },
    }
}
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chaohu'
    

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASES_URI='mysql+pymysql://root:root@localhost/db_spring'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASES_URI='mysql+pymysql://root:root@localhost/db_spring'
    
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}