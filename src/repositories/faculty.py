from flask import abort
from models import Faculty
from sqlalchemy.exc import IntegrityError


class FacultyRepository:
  @staticmethod
  def get(id):
      try:
        return Faculty.query.get(id)
      except IntegrityError:
        abort(404, 'Faculty not found')

  @staticmethod
  def get_all():
    return Faculty.query.all()

  def update(id, **kwargs):
    faculty = Faculty.query.get(id)
    faculty.update(**kwargs)
    return faculty.save()

  def delete(id):
    faculty = Faculty.query.get(id)
    return faculty.delete()

  @staticmethod
  def create(**kwargs):
    faculty = Faculty(**kwargs)
    return faculty.save()
