from src.models import Group

class GroupRepository:
  @staticmethod
  def get(id):
    return Group.query.get_or_404(id)

  @staticmethod
  def get_all(**kwargs):
    groups = Group.query
    faculty_id = kwargs.get('faculty_id', None)
    if faculty_id is not None:
      groups = groups.filter(faculty_id=faculty_id)
    return groups.all()

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
