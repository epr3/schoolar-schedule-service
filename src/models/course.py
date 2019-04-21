from sqlalchemy_utils import UUIDType
from marshmallow import Schema, fields
from . import db, SubjectSchema
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class Course(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'courses'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    course_path = db.Column(db.String, nullable=False)
    subjectId = db.Column(db.String, db.ForeignKey(
        'subjects.id', ondelete='CASCADE'), nullable=False)
    subject = db.relationship(
        'Subject', backref=db.backref('course_subjects', lazy='dynamic'), foreign_keys=[subjectId])

class CourseSchema(Schema):
    id = fields.Str(dump_only=True)
    course_path = fields.Str(required=True)
    subjectId = fields.Str(required=True, load_only=True)
    subject = fields.Nested(SubjectSchema)
