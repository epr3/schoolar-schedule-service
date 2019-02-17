from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from repositories import FacultyRepository
from util import parse_params

class FacultyResource(Resource):
  def get(self, id):
    return FacultyRepository.get(id)

  @parse_params(
      Argument(
          'name',
          location='json',
          required=False,
          help='The faculty name'
      )
  )
  def put(self, id, name):
    return FacultyRepository.update(id, name=name)

  def delete(self, id):
    return FacultyRepository.delete(id)

class FacultyListResource(Resource):
  @parse_params(
      Argument(
          'name',
          location='json',
          required=True,
          help='The faculty name'
      )
  )
  def post(self, name):
    faculty = FacultyRepository.create(name=name)
    return faculty

  def get(self):
    return FacultyRepository.get_all()
