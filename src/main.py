# ! python3
# -*- coding: utf-8 -*-

"""
In this module app instance and database
will be created.
"""

import os
from flask import Flask
from flask import jsonify
from api.utils.database import db

def create_app(config):
    """
    This function is responsible of create the app
    instance in with the parameters provided in
    the config file.
    """

    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

if __name__ == '__main__':
    app.run(port=5000, hots='0.0.0.0', use_reloader=False)
