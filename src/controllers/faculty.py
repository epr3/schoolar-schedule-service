from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError

from repositories import FacultyRepository
from models import FacultySchema

faculty_schema = FacultySchema()
faculties_schema = FacultySchema(many=True)

class FacultyResource(Resource):
  def get(self, id):
    return jsonify({'faculty': faculty_schema.dump(FacultyRepository.get(id))})

  def put(self, id):
    json_data = request.get_json()
    try:
      data = faculty_schema.load(json_data)
    except ValidationError as err:
      return jsonify(err.messages), 422
    return FacultyRepository.update(id, data)

  def delete(self, id):
    return FacultyRepository.delete(id)

class FacultyListResource(Resource):
  def post(self):
    json_data = request.get_json()
    try:
      data = faculty_schema.load(json_data)
    except ValidationError as err:
      return jsonify(err.messages), 422
    return jsonify({'faculty': faculty_schema.dump(FacultyRepository.create(data))})

  def get(self):
    return jsonify({ 'faculties': faculties_schema.dump(FacultyRepository.get_all()) })
