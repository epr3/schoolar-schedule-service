from . import db, ma
from marshmallow import Schema, fields
from uuid import uuid4


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.String, primary_key=True, default=uuid4)
    course_path = db.Column(db.String, nullable=False)
    subject_id = db.Column(db.String, db.ForeignKey(
        'subjects.id', ondelete='CASCADE'), nullable=False)
    subject = db.relationship(
        'Subject', backref=db.backref('subjects', lazy='dynamic'))
    professor_id = db.Column(db.String, nullable=False)

    def __init__(self, course, subject_id):
        self.course = course
        self.subject_id = subject_id


class CourseSchema(ma.ModelSchema):
    class Meta:
        model = Course
