from flask import Blueprint
from flask_restx import Api
from .restv2.api_user.user import hello_namespace
from .restv2.api_admin.admin import admin_namespace
from .restv2.api_admin.add_admin import create_admin_namespace

learn_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api_v2 = Api(
    learn_blueprint,
    title='api_v2',
    version='2.0',
    description='A description',
)

api_v2.add_namespace(hello_namespace)
api_v2.add_namespace(admin_namespace)
api_v2.add_namespace(create_admin_namespace)