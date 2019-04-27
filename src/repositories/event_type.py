from src.models import EventType


class EventTypeRepository:
  @staticmethod
  def get(id):
    return EventType.query.get_or_404(id)

  @staticmethod
  def get_all():
    return EventType.query.all()

  def update(id, **kwargs):
    faculty = EventType.query.get(id)
    faculty.update(**kwargs)
    return faculty.save()

  def delete(id):
    faculty = EventType.query.get(id)
    return faculty.delete()

  @staticmethod
  def create(**kwargs):
    faculty = EventType(**kwargs)
    return faculty.save()
