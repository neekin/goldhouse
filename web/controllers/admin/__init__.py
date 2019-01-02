from flask_admin import BaseView, expose, AdminIndexView


class AdminIndexView(BaseView):

    def __init__(self, name=None, category=None,
                 endpoint=None, url=None,
                 template='admin/index.html'):
        super(AdminIndexView, self).__init__(name or babel.lazy_gettext('Home'),
                                             category,
                                             endpoint or 'ace',
                                             url or '/ace',
                                             'static')
        self._template = template

    @expose()
    def index(self):
        return self.render(self._template)
