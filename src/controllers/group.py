from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src.repositories import GroupRepository
from src.models import GroupSchema

group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)


class GroupResource(Resource):
  def get(self, id):
    return group_schema.dump(GroupRepository.get(id))

  def put(self, id):
    json_data = request.get_json()
    try:
      data = group_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return group_schema.dump(GroupRepository.update(id, **data))

  def delete(self, id):
    return GroupRepository.delete(id), 204


class GroupListResource(Resource):
  def post(self):
    json_data = request.get_json()
    try:
      data = group_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return group_schema.dump(GroupRepository.create(**data))

  def get(self):
    return groups_schema.dump(GroupRepository.get_all(**request.args))
