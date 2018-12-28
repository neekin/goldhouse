from flask import Blueprint

route_index = Blueprint('index', __name__)

import web.controllers.index
