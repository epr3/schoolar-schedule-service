from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

from src.repositories import SubjectRepository
from src.models import SubjectSchema

from src.util import roles_required

subject_schema = SubjectSchema()
subjects_schema = SubjectSchema(many=True)


class SubjectResource(Resource):
  @jwt_required
  def get(self, id):
    return subject_schema.dump(SubjectRepository.get(id))

  @jwt_required
  @roles_required(['ADMIN'])
  def put(self, id):
    json_data = request.get_json()
    try:
      data = subject_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return subject_schema.dump(SubjectRepository.update(id, **data))

  @jwt_required
  @roles_required(['ADMIN'])
  def delete(self, id):
    return SubjectRepository.delete(id), 204


class SubjectListResource(Resource):
  @jwt_required
  @roles_required(['ADMIN'])
  def post(self):
    json_data = request.get_json()
    try:
      data = subject_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return subject_schema.dump(SubjectRepository.create(**data))

  @jwt_required
  def get(self):
    return subjects_schema.dump(SubjectRepository.get_all(**request.args))
