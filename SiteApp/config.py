import os
from os import environ as env
from urllib.parse import urlunparse
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(usecwd=True))


def create_database_url():
    engine = env.get('DATABASE_ENGINE')
    user = env.get('DATABASE_USER')
    password = env.get('DATABASE_PASS')
    host = env.get('DATABASE_HOST')
    port = env.get('DATABASE_PORT')
    db_name = env.get('DATABASE_NAME')
    return urlunparse((engine, f'{user}:{password}@{host}:{port}', db_name, None, None, None))


class Config:

    SECRET_KEY = env.get('SECRET_KEY')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_database_url()


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    """ Use this config for testing """
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
