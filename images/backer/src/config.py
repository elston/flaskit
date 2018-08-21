# -*- coding: utf-8 -*-

import json
import os
import logging
from logging.handlers import RotatingFileHandler

# ...
class ImproperlyConfigured(Exception):
    pass

# ...
def get_env_variable(var_name, default='None'):
    try:
        return os.environ[var_name]
    except KeyError:
        # ..
        if default == 'None':
            err_msg = "Set the %s environment variable" % var_name
            raise ImproperlyConfigured(err_msg)
        # ...
        return default


class BaseConfig(object):

    DEBUG = False
    TESTING = False

    # ...dir
    PROJECT_PATH = os.path.dirname(
        os.path.abspath(__file__)
    )
    # PROJECT_ROOT = os.path.abspath(
    #     os.path.join(
    #         PROJECT_PATH, os.pardir
    #     )
    # )
    # APP_DIR = PROJECT_PATH
    # print(PROJECT_ROOT, PROJECT_PATH)
    

    # ...templates
    TEMPLATE_FOLDER = os.path.join(
        PROJECT_PATH, 'templates'
    )


    # ..kyes
    SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'


    # ..logs
    # LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_FORMAT = (
        '%(asctime)s [%(levelname)s]: %(message)s ',
        '%Y-%m-%d %H:%M:%S'        
    )
    LOGGING_LOCATION = os.path.join(
        PROJECT_PATH, '.logs/main.log'
    )
    LOGGING_SIZE = 52428800  
    LOGGING_LEVEL = logging.INFO



    # ...databases
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        'postgresql+psycopg2://{user}:{pw}@{url}:5432/{db}'
    ).format(
        user=get_env_variable('DB_USER'),
        pw=get_env_variable('DB_PASSWORD'),
        url=get_env_variable('DB_URL'),
        db=get_env_variable('DB_NAME')
    )

    # ...bcrypt
    BCRYPT_LOG_ROUNDS = 13

    # ..webpack manifest
    WEBPACK_MANIFEST_PATH = os.path.join(
        '/', 'fronter', 'build','manifest.json'
    )
    WEBPACK_ASSETS_URL = '/build'

    # ..
    MIGRATION_MODE = json.loads(
        get_env_variable('MIGRATION_MODE', 'false'))

class DevelopmentConfig(BaseConfig):

    # ...
    DEBUG = True
    TESTING = False

    # ..kyes
    SECRET_KEY = 'a9eec0e0-23b7-4788-9a92-318347b9a39f'

    # ... logging
    LOGGING_LEVEL = logging.DEBUG


class TestingConfig(BaseConfig):

    DEBUG = False
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = '792842bc-c4df-4de1-9177-d5207bd9faa6'


class ProductionConfig(BaseConfig):

    SECRET_KEY = get_env_variable('DB_SECRET_KEY')


class Config(object):

    config_obj = {
        "production": "config.ProductionConfig",
        "development": "config.DevelopmentConfig",
        "testing": "config.TestingConfig",
    }


    def init_app(self, app):
        # ...
        config_name = os.getenv('FLASK_CONFIGURATION', 'base')
        app.config.from_object(self.config_obj[config_name])

        # logging
        # ...
        formatter = logging.Formatter(*app.config['LOGGING_FORMAT'])
        handler = RotatingFileHandler(
            app.config['LOGGING_LOCATION']
            , maxBytes = app.config['LOGGING_SIZE']
            , backupCount = 5)
        # ...
        handler.setLevel(app.config['LOGGING_LEVEL'])
        handler.setFormatter(formatter)    
        app.logger.addHandler(handler)

        # ..templates
        template_folder = app.config.get('TEMPLATE_FOLDER',None)
        if template_folder:
            app.template_folder = template_folder

