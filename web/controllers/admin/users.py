from flask_admin import BaseView, expose


class UsersView(BaseView):
    @expose('/')
    def index(self):
        return self.render('ace/users.html')

    @expose('/second_page')
    def second_page(self):
        return self.render('ace/second_page.html')
