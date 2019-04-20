from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

from src.repositories import CourseRepository
from src.models import CourseSchema

from src.util import roles_required

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)


class CourseResource(Resource):
  @jwt_required
  def get(self, id):
    return course_schema.dump(CourseRepository.get(id))

  @jwt_required
  @roles_required(['ADMIN'])
  def put(self, id):
    json_data = request.get_json()
    try:
      data = course_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return course_schema.dump(CourseRepository.update(id, **data))

  @jwt_required
  @roles_required(['ADMIN'])
  def delete(self, id):
    return CourseRepository.delete(id), 204


class CourseListResource(Resource):
  @jwt_required
  @roles_required(['ADMIN'])
  def post(self):
    json_data = request.get_json()
    try:
      data = course_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return course_schema.dump(CourseRepository.create(**data))

  @jwt_required
  def get(self):
    return courses_schema.dump(CourseRepository.get_all())
