from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

from src.repositories import FacultyRepository
from src.models import FacultySchema
from src.util import roles_required

faculty_schema = FacultySchema()
faculties_schema = FacultySchema(many=True)

class FacultyResource(Resource):
  def get(self, id):
    return faculty_schema.dump(FacultyRepository.get(id))

  def put(self, id):
    json_data = request.get_json()
    try:
      data = faculty_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return faculty_schema.dump(FacultyRepository.update(id, **data))

  def delete(self, id):
    return FacultyRepository.delete(id), 204

class FacultyListResource(Resource):
  @jwt_required
  def post(self):
    json_data = request.get_json()
    try:
      data = faculty_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return faculty_schema.dump(FacultyRepository.create(**data))

  @jwt_required
  @roles_required(['ADMIN', 'STUDENT'])
  def get(self):
    return faculties_schema.dump(FacultyRepository.get_all())
