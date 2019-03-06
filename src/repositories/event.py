from models import Event


class EventRepository:
  @staticmethod
  def get(id):
    return Event.query.get_or_404(id)

  @staticmethod
  def get_all():
    return Event.query.all()

  def update(id, **kwargs):
    event = Event.query.get(id)
    event.update(**kwargs)
    return event.save()

  def delete(id):
    event = Event.query.get(id)
    return event.delete()

  @staticmethod
  def create(**kwargs):
    event = Event(**kwargs)
    return event.save()
