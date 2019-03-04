from flask import abort
from models import Subject
from sqlalchemy.exc import IntegrityError


class SubjectRepository:
  @staticmethod
  def get(id):
    try:
      return Subject.query.get(id)
    except IntegrityError:
      abort(404, 'Subject not found')

  @staticmethod
  def get_all():
    return Subject.query.all()

  def update(id, **kwargs):
    subject = Subject.query.get(id)
    subject.update(**kwargs)
    return subject.save()

  def delete(id):
    subject = Subject.query.get(id)
    return subject.delete()

  @staticmethod
  def create(**kwargs):
    subject = Subject(**kwargs)
    return subject.save()
