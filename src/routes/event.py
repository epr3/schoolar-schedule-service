from flask import Blueprint
from src.util import SchoolarApi

from src.controllers import EventResource, EventListResource


EVENT_BLUEPRINT = Blueprint('event', __name__)

SchoolarApi(EVENT_BLUEPRINT).add_resource(
    EventListResource,
    '/events'
)

SchoolarApi(EVENT_BLUEPRINT).add_resource(
    EventResource,
    '/events/<string:id>'
)
