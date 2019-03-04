from marshmallow import Schema, fields
from . import db, FacultySchema
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class Subject(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'subjects'
    id = db.Column(db.String, primary_key=True, default=str(uuid4()))
    name = db.Column(db.String, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.String, db.ForeignKey(
        'faculties.id', ondelete='CASCADE'), nullable=False)
    faculty = db.relationship(
        'Faculty', backref=db.backref('subject_faculties', lazy='dynamic'), foreign_keys=[faculty_id])


class SubjectSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    credits = fields.Int(required=True)
    faculty = fields.Nested(FacultySchema)
