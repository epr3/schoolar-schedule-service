from sqlalchemy_utils import UUIDType
from marshmallow import Schema, fields
from . import db, FacultySchema
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class Group(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'groups'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    number = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    facultyId = db.Column(UUIDType(binary=False), db.ForeignKey(
        'faculties.id', ondelete='CASCADE'), nullable=False)
    faculty = db.relationship('Faculty', viewonly=True)


class GroupSchema(Schema):
    id = fields.Str(dump_only=True)
    number = fields.Str(required=True)
    year = fields.Str(required=True)
    facultyId = fields.Str(required=True, load_only=True)
    faculty = fields.Nested(FacultySchema)
