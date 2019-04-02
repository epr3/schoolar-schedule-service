from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src.repositories import SubjectRepository
from src.models import SubjectSchema

subject_schema = SubjectSchema()
subjects_schema = SubjectSchema(many=True)


class SubjectResource(Resource):
  def get(self, id):
    return subject_schema.dump(SubjectRepository.get(id))

  def put(self, id):
    json_data = request.get_json()
    try:
      data = subject_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return subject_schema.dump(SubjectRepository.update(id, **data))

  def delete(self, id):
    return SubjectRepository.delete(id), 204


class SubjectListResource(Resource):
  def post(self):
    json_data = request.get_json()
    try:
      data = subject_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return subject_schema.dump(SubjectRepository.create(**data))

  def get(self):
    return subjects_schema.dump(SubjectRepository.get_all())
