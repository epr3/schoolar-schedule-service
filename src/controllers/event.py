from datetime import datetime
from dateutil import parser
from pytz import UTC
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from dateutil.rrule import rrule, WEEKLY, DAILY

from repositories import EventRepository
from models import EventSchema

event_schema = EventSchema()
events_schema = EventSchema(many=True)


class EventResource(Resource):
  def get(self, id):
    return event_schema.dump(EventRepository.get(id))

  def put(self, id):
    json_data = request.get_json()
    try:
      data = event_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return event_schema.dump(EventRepository.update(id, **data))

  def delete(self, id):
    return EventRepository.delete(id), 204


class EventListResource(Resource):
  def post(self):
    json_data = request.get_json()
    try:
      data = event_schema.load(json_data)
    except ValidationError as err:
      return err.messages, 422
    return event_schema.dump(EventRepository.create(**data))

  def get(self):
    events = events_schema.dump(EventRepository.get_all(**request.args))
    if request.args.get('start_date'):
      start = parser.parse(request.args.get('start_date'))
    if request.args.get('end_date'):
      end = parser.parse(request.args.get('end_date'))
    if start and end:
      event_list = [{
        **event,
        'dates': [datetime.strftime(item, '%Y-%m-%d %H:%M:%S') for item in list(rrule(WEEKLY if event['frequency'] == 'WEEKLY' else DAILY, dtstart=parser.parse(event['start_date']), until=parser.parse(event['end_date']), interval=event['interval'])) if item >= UTC.localize(start) and item <= UTC.localize(end)]} for event in events]

      return event_list

    return events
