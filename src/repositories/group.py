from flask import abort
from models import Group
from sqlalchemy.exc import IntegrityError

class GroupRepository:
  @staticmethod
  def get(id):
    try:
      return Group.query.get(id)
    except IntegrityError:
      abort(404, 'Group not found')

  @staticmethod
  def get_all():
    return Group.query.all()

  def update(id, **kwargs):
    group = Group.query.get(id)
    group.update(**kwargs)
    return group.save()

  def delete(id):
    group = Group.query.get(id)
    return group.delete()

  @staticmethod
  def create(**kwargs):
    group = Group(**kwargs)
    return group.save()
