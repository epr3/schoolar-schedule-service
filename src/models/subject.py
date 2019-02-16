from . import db, ma
from marshmallow import Schema, fields
from uuid import uuid4


class Subject(db.Model):
  __tablename__ = 'subjects'
  id = db.Column(db.String, primary_key=True, default=uuid4)
  name = db.Column(db.String, nullable=False)
  credits = db.Column(db.String, nullable=False)
  faculty_id = db.Column(db.String, db.ForeignKey(
      'faculties.id', ondelete='CASCADE'), nullable=False)
  faculty = db.relationship(
      'Faculty', backref=db.backref('faculties', lazy='dynamic'))

  def __init__(self, subject, faculty_id):
    self.subject = subject
    self.faculty_id = faculty_id


class SubjectSchema(ma.Schema):
  id = fields.String()
  name = fields.String(required=True)
  credits = fields.String(required=True)
  faculty_id = fields.String(required=True)
