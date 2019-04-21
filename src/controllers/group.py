from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

from src.repositories import GroupRepository
from src.models import GroupSchema

from src.util import roles_required

group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)


class GroupResource(Resource):
  @jwt_required
  def get(self, id):
    # import pdb; pdb.set_trace()
    return group_schema.dump(GroupRepository.get(id))

  @jwt_required
  @roles_required(['ADMIN'])
  def put(self, id):
    json_data = request.get_json()
    try:
      data = group_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return group_schema.dump(GroupRepository.update(id, **data))

  @jwt_required
  @roles_required(['ADMIN'])
  def delete(self, id):
    return GroupRepository.delete(id), 204


class GroupListResource(Resource):
  @jwt_required
  @roles_required(['ADMIN'])
  def post(self):
    json_data = request.get_json()
    try:
      data = group_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return group_schema.dump(GroupRepository.create(**data))

  @jwt_required
  def get(self):
    return groups_schema.dump(GroupRepository.get_all(**request.args))
