from . import db, ma
from marshmallow import Schema, fields
from uuid import uuid4


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.String, primary_key=True, default=uuid4)
    room = db.Column(db.String, nullable=False)
    rrule = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    is_notifiable = db.Column(db.Boolean, default=False)
    subject_id = db.Column(db.String, db.ForeignKey(
        'subjects.id', ondelete='CASCADE'), nullable=False)
    subject = db.relationship(
        'Subject', backref=db.backref('subjects', lazy='dynamic'))
    group_id = db.Column(db.String, db.ForeignKey(
        'groups.id', ondelete='CASCADE'), nullable=False)
    group = db.relationship(
        'Group', backref=db.backref('groups', lazy='dynamic'))
    professor_id = db.Column(db.String, nullable=False)

    def __init__(self, event, group_id, subject_id):
        self.event = event
        self.group_id = group_id
        self.subject_id = subject_id


class EventSchema(ma.Schema):
    id = fields.String()
    room = fields.String(required=True)
    rrule = fields.String(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    is_notifiable = fields.Boolean()
    subject_id = fields.String(required=True)
    group_id = fields.String(required=True)
    professor_id = fields.String(required=True)
