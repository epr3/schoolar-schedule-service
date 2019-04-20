from marshmallow import Schema, fields
from . import db, FacultySchema
from .abstract import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Subject(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'subjects'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    facultyId = db.Column(db.String, db.ForeignKey(
        'faculties.id', ondelete='CASCADE'), nullable=False)
    faculty = db.relationship(
        'Faculty', backref=db.backref('subject_faculties', lazy='dynamic'), foreign_keys=[facultyId])


class SubjectSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    credits = fields.Int(required=True)
    facultyId = fields.Str(required=True, load_only=True)
    faculty = fields.Nested(FacultySchema)
