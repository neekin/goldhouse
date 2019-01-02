from . import route_index


@route_index.route("/")
def index():
    return 'Hello World'


# from .ace.users import AdminView
# from application import ace
#
# ace.add_view(AdminView)
