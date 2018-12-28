from flask import Blueprint

api_index = Blueprint('api', __name__)


@api_index.route("/")
def index():
    return 'api server hahah ^_^'


import web.api.member
