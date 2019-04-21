from src.models import Event
from src.util import is_valid_date


class EventRepository:
    @staticmethod
    def get(id):
        return Event.query.get_or_404(id)

    @staticmethod
    def get_all(**kwargs):
        events = Event.query
        startDate = kwargs.get('startDate', None)
        endDate = kwargs.get('endDate', None)
        groupId = kwargs.get('groupId', None)
        professorId = kwargs.get('professorId', None)

        if startDate is not None and is_valid_date(startDate):
            events = events.filter(Event.end_date >= startDate)
        if endDate is not None and is_valid_date(endDate):
            events = events.filter(Event.startDate <= endDate)
        if groupId is not None:
            events = events.filter(Event.groupId == groupId)
        if professorId is not None:
            events = events.filter(Event.professorId == professorId)
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
