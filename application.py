from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        self.config.from_pyfile('config/base.py')
        self.config.from_pyfile('config/local.py')


def registerblueprints(app):
    from web.controllers.index import route_index
    app.register_blueprint(route_index, url_prefix='/')
    from web.api import api_index
    app.register_blueprint(api_index, url_prefix='/api')


def createApp():
    app = Application(__name__)
    db.init_app(app)
    registerblueprints(app)

    return app
