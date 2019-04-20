from marshmallow import Schema, fields
from . import db, SubjectSchema, GroupSchema
from .abstract import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Event(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'events'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    room = db.Column(db.String)
    interval = db.Column(db.Integer, nullable=False)
    frequency = db.Column(db.String, nullable=False)
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    isFullDay = db.Column(db.Boolean, default=False)
    isNotifiable = db.Column(db.Boolean, default=False)
    subjectId = db.Column(db.String, db.ForeignKey(
        'subjects.id', ondelete='CASCADE'))
    subject = db.relationship(
        'Subject', backref=db.backref('event_subjects', lazy='dynamic'), foreign_keys=[subjectId])
    groupId = db.Column(db.String, db.ForeignKey(
        'groups.id', ondelete='CASCADE'), nullable=False)
    group = db.relationship(
        'Group', backref=db.backref('event_groups', lazy='dynamic'), foreign_keys=[groupId])
    userId = db.Column(db.String)


class EventSchema(Schema):
    id = fields.Str(dump_only=True)
    room = fields.Str(required=True)
    interval = fields.Int(required=True)
    frequency = fields.Str(required=True)
    startDate = fields.DateTime(required=True)
    endDate = fields.DateTime(required=True)
    duration = fields.Integer(required=True)
    isFullDay = fields.Bool()
    isNotifiable = fields.Bool()
    subjectId = fields.Str(required=True, load_only=True)
    groupId = fields.Str(required=True, load_only=True)
    userId = fields.Str(required=True, load_only=True)
    subject = fields.Nested(SubjectSchema)
    group = fields.Nested(GroupSchema)

