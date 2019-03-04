from marshmallow import Schema, fields
from . import db, SubjectSchema
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class Course(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'courses'
    id = db.Column(db.String, primary_key=True, default=str(uuid4()))
    course_path = db.Column(db.String, nullable=False)
    subject_id = db.Column(db.String, db.ForeignKey(
        'subjects.id', ondelete='CASCADE'), nullable=False)
    subject = db.relationship(
        'Subject', backref=db.backref('course_subjects', lazy='dynamic'), foreign_keys=[subject_id])
    professor_id = db.Column(db.String, nullable=False)

class CourseSchema(Schema):
    id = fields.Str(dump_only=True)
    course_path = fields.Str(required=True)
    subject = fields.Nested(SubjectSchema)
