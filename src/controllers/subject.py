from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from repositories import SubjectRepository
from util import parse_params


class SubjectResource(Resource):
  def get(self, id):
    return SubjectRepository.get(id)

  @parse_params(
      Argument(
          'name',
          location='json',
          required=False,
          help='The subject name'
      ),
      Argument(
          'credits',
          location='json',
          required=False,
          help='The subject credits'
      ),
      Argument(
          'faculty_id',
          location='json',
          required=False,
          help='The subject faculty id'
      )
  )
  def put(self, id, name, credits, faculty_id):
    return SubjectRepository.update(id, name=name, credits=credits, faculty_id=faculty_id)

  def delete(self, id):
    return SubjectRepository.delete(id)


class SubjectListResource(Resource):
  @parse_params(
      Argument(
          'name',
          location='json',
          required=True,
          help='The subject name'
      ),
      Argument(
        'credits',
        location='json',
        required=True,
        help='The subject credits'
      ),
      Argument(
          'faculty_id',
          location='json',
          required=True,
          help='The subject faculty id'
      )
  )
  def post(self, name, credits, faculty_id):
    subject = SubjectRepository.create(name=name, credits=credits, faculty_id=faculty_id)
    return subject

  def get(self):
    return SubjectRepository.get_all()
