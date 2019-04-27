from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

from src.repositories import EventTypeRepository
from src.models import EventTypeSchema
from src.util import roles_required

event_type_schema = EventTypeSchema()
event_types_schema = EventTypeSchema(many=True)


class EventTypeResource(Resource):
  @jwt_required
  def get(self, id):
    # import pdb; pdb.set_trace()
    return event_type_schema.dump(EventTypeRepository.get(id))

  @jwt_required
  @roles_required(['ADMIN'])
  def put(self, id):
    json_data = request.get_json()
    try:
      data = event_type_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return event_type_schema.dump(EventTypeRepository.update(id, **data))

  @jwt_required
  @roles_required(['ADMIN'])
  def delete(self, id):
    return EventTypeRepository.delete(id), 204


class EventTypeListResource(Resource):
  @jwt_required
  @roles_required(['ADMIN'])
  def post(self):
    json_data = request.get_json()
    try:
      data = event_type_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return event_type_schema.dump(EventTypeRepository.create(**data))

  @jwt_required
  def get(self):
    return event_types_schema.dump(EventTypeRepository.get_all())
