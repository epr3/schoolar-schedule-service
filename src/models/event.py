from marshmallow import Schema, fields
from . import db, SubjectSchema, GroupSchema
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class Event(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'events'
    id = db.Column(db.String, primary_key=True, default=str(uuid4()))
    room = db.Column(db.String, nullable=False)
    rrule = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    is_full_day = db.Column(db.Boolean, default=False)
    is_notifiable = db.Column(db.Boolean, default=False)
    subject_id = db.Column(db.String, db.ForeignKey(
        'subjects.id', ondelete='CASCADE'), nullable=False)
    subject = db.relationship(
        'Subject', backref=db.backref('event_subjects', lazy='dynamic'), foreign_keys=[subject_id])
    group_id = db.Column(db.String, db.ForeignKey(
        'groups.id', ondelete='CASCADE'), nullable=False)
    group = db.relationship(
        'Group', backref=db.backref('event_groups', lazy='dynamic'), foreign_keys=[group_id])
    professor_id = db.Column(db.String, nullable=False)


class EventSchema(Schema):
    id = fields.Str(dump_only=True)
    room = fields.Str(required=True)
    rrule = fields.Str(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    is_full_day = fields.Bool()
    is_notifiable = fields.Bool()
    subject = fields.Nested(SubjectSchema)
    group = fields.Nested(GroupSchema)

