from datetime import datetime, timedelta
from dateutil import parser
from pytz import UTC
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from dateutil.rrule import rrule, WEEKLY, DAILY

from src.repositories import EventRepository
from src.models import EventSchema

from src.util import exclude_keys, roles_required

event_schema = EventSchema()
events_schema = EventSchema(many=True)


class EventResource(Resource):
    @jwt_required
    def get(self, id):
        return event_schema.dump(EventRepository.get(id))

    @jwt_required
    @roles_required(['ADMIN'])
    def put(self, id):
        json_data = request.get_json()
        try:
            data = event_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        return event_schema.dump(EventRepository.update(id, **data))

    @jwt_required
    @roles_required(['ADMIN'])
    def delete(self, id):
        return EventRepository.delete(id), 204


class EventListResource(Resource):
    @jwt_required
    @roles_required(['ADMIN'])
    def post(self):
        json_data = request.get_json()
        try:
            data = event_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        return event_schema.dump(EventRepository.create(**data))

    @jwt_required
    def get(self):
        events = events_schema.dump(EventRepository.get_all(**request.args))
        start = None
        end = None
        if request.args.get('startDate'):
            start = parser.parse(request.args.get('startDate'))
        if request.args.get('endDate'):
            end = parser.parse(request.args.get('endDate'))
        if start and end:
            event_list = [{**exclude_keys(event, {'duration', 'interval'}), 'start_date': datetime.strftime(item, '%Y-%m-%d %H:%M:%S'), 'end_date': datetime.strftime(item + timedelta(seconds=event['duration']), '%Y-%m-%d %H:%M:%S')} for event in events for item in list(rrule(
                WEEKLY if event['frequency'] == 'WEEKLY' else DAILY, dtstart=parser.parse(event['start_date']), until=parser.parse(event['end_date']), interval=event['interval'])) if item >= UTC.localize(start) and item <= UTC.localize(end)]

            return event_list

        return events
