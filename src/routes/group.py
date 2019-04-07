from flask import Blueprint
from src.util import SchoolarApi

from src.controllers import GroupResource, GroupListResource


GROUP_BLUEPRINT = Blueprint('group', __name__)

SchoolarApi(GROUP_BLUEPRINT).add_resource(
    GroupListResource,
    '/groups'
)

SchoolarApi(GROUP_BLUEPRINT).add_resource(
    GroupResource,
    '/groups/<string:id>'
)
