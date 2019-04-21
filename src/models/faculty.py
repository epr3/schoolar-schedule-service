from sqlalchemy_utils import UUIDType
from marshmallow import Schema, fields
from . import db
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class Faculty(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'faculties'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    name = db.Column(db.String, nullable=False)


class FacultySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
