from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from repositories import CourseRepository
from models import CourseSchema

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)


class CourseResource(Resource):
  def get(self, id):
    return course_schema.dump(CourseRepository.get(id))

  def put(self, id):
    json_data = request.get_json()
    try:
      data = course_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return course_schema.dump(CourseRepository.update(id, **data))

  def delete(self, id):
    return CourseRepository.delete(id), 204


class CourseListResource(Resource):
  def post(self):
    json_data = request.get_json()
    try:
      data = course_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return course_schema.dump(CourseRepository.create(**data))

  def get(self):
    return courses_schema.dump(CourseRepository.get_all())
