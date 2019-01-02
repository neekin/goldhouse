from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
import time

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
    addAdminView(app)
    return app


def addAdminView(app):
    index_view = AdminIndexView(template='ace/master.html', name='系统管理', menu_icon_type='fa',
                                menu_icon_value='menu-icon fa fa-desktop')
    admin = Admin(name="金房源", index_view=index_view)
    from web.controllers.admin.users import UsersView
    users_view = UsersView(name='用户管理', menu_icon_type='fa', menu_icon_value='menu-icon fa-user')
    admin.add_view(users_view)
    admin.init_app(app)


def log(*args, **kwargs):
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('tmp/log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)
