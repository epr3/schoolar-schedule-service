from flask import Blueprint
from flask_restful import Api

from src.controllers import GroupResource, GroupListResource


GROUP_BLUEPRINT = Blueprint('group', __name__)

Api(GROUP_BLUEPRINT).add_resource(
    GroupListResource,
    '/groups'
)

Api(GROUP_BLUEPRINT).add_resource(
    GroupResource,
    '/groups/<string:id>'
)
