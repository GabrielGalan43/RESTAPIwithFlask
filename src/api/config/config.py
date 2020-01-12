# ! python3
# -*- coding: utf-8 -*-

"""
Configuration parameters that will be
loaded from main.py, to start the app.
"""


class Config:
    """
    Main class configuration parameters.
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Parameters for app running in production mode.
    """
    SQLALCHEMY_DATABASE_URI = "Production DB URL"


class DevelopmentConfig(Config):
    """
    Parameters for app in development mode.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'Development DB URL'
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    """
    Parameters for app in testing mode.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'Testing DB URL'
    SQLALCHEMY_ECHO = False
