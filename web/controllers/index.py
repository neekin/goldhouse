from . import route_index


@route_index.route("/")
def index():
    return 'Index'
