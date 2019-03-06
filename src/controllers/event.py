from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from repositories import EventRepository
from models import EventSchema

event_schema = EventSchema()
events_schema = EventSchema(many=True)


class EventResource(Resource):
  def get(self, id):
    return event_schema.dump(EventRepository.get(id))

  def put(self, id):
    json_data = request.get_json()
    try:
      data = event_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return event_schema.dump(EventRepository.update(id, **data))

  def delete(self, id):
    return EventRepository.delete(id), 204


class EventListResource(Resource):
  def post(self):
    json_data = request.get_json()
    try:
      data = event_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return event_schema.dump(EventRepository.create(**data))

  def get(self):
    # TODO: parse query params here and return list of events
    return events_schema.dump(EventRepository.get_all())
