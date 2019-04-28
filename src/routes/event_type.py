from flask import Blueprint
from src.util import SchoolarApi

from src.controllers import EventTypeListResource, EventTypeResource


EVENT_TYPE_BLUEPRINT = Blueprint('event_type', __name__)

SchoolarApi(EVENT_TYPE_BLUEPRINT).add_resource(
    EventTypeListResource,
    '/event_types'
)

SchoolarApi(EVENT_TYPE_BLUEPRINT).add_resource(
    EventTypeResource,
    '/event_types/<string:id>'
)
