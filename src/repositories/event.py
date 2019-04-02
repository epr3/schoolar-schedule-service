from src.models import Event
from src.util import is_valid_date


class EventRepository:
  @staticmethod
  def get(id):
    return Event.query.get_or_404(id)

  @staticmethod
  def get_all(**kwargs):
    events = Event.query
    start_date = kwargs.get('start_date', None)
    end_date = kwargs.get('end_date', None)
    group_id = kwargs.get('group_id', None)
    professor_id = kwargs.get('professor_id', None)

    if start_date is not None and is_valid_date(start_date):
      events = events.filter(Event.end_date >= start_date)
    if end_date is not None and is_valid_date(end_date):
      events = events.filter(Event.start_date <= end_date)
    if group_id is not None:
      events = events.filter(group_id=group_id)
    if professor_id is not None:
      events = events.filter(professor_id=professor_id)
    return events.all()

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
