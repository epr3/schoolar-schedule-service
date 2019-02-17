from . import db, ma
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class Subject(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'subjects'
    id = db.Column(db.String, primary_key=True, default=uuid4)
    name = db.Column(db.String, nullable=False)
    credits = db.Column(db.String, nullable=False)
    faculty_id = db.Column(db.String, db.ForeignKey(
        'faculties.id', ondelete='CASCADE'), nullable=False)
    faculty = db.relationship(
        'Faculty', backref=db.backref('subject_faculties', lazy='dynamic'), foreign_keys=[faculty_id])

    def __init__(self, subject, faculty_id):
        self.subject = subject
        self.faculty_id = faculty_id


class SubjectSchema(ma.ModelSchema):
    class Meta:
        model = Subject
