from flask import Blueprint
from flask_restful import Api

from controllers import EventResource, EventListResource


EVENT_BLUEPRINT = Blueprint('event', __name__)

Api(EVENT_BLUEPRINT).add_resource(
    EventListResource,
    '/events'
)

Api(EVENT_BLUEPRINT).add_resource(
    EventResource,
    '/events/<string:id>'
)
