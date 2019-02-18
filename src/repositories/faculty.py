from flask import jsonify
from models import Faculty, FacultySchema

faculty_schema = FacultySchema()
faculties_schema = FacultySchema(many=True)


class FacultyRepository:
  @staticmethod
  def get(id):
    return faculty_schema.jsonify(Faculty.query.get(id))

  @staticmethod
  def get_all():
    result = faculties_schema.dump(Faculty.query.all())
    return jsonify(result.data)

  def update(id, **kwargs):
    faculty = Faculty.query.get(id)
    faculty.update(**kwargs)
    return faculty_schema.jsonify(faculty.save())

  def delete(id):
    faculty = Faculty.query.get(id)
    return faculty.delete()

  @staticmethod
  def create(**kwargs):
    faculty = Faculty(**kwargs)
    return faculty_schema.jsonify(faculty.save())
