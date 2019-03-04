from marshmallow import Schema, fields
from . import db, FacultySchema
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class Group(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'groups'
    id = db.Column(db.String, primary_key=True, default=str(uuid4()))
    number = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    faculty_id = db.Column(db.String, db.ForeignKey(
        'faculties.id', ondelete='CASCADE'), nullable=False)
    faculty = db.relationship(
        'Faculty', backref=db.backref('group_faculties', lazy='dynamic'), foreign_keys=[faculty_id])


class GroupSchema(Schema):
    id = fields.Str(dump_only=True)
    number = fields.Str(required=True)
    year = fields.Str(required=True)
    faculty = fields.Nested(FacultySchema)
