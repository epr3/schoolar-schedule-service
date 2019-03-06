from models import Group

class GroupRepository:
  @staticmethod
  def get(id):
    return Group.query.get_or_404(id)

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
