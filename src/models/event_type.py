from sqlalchemy_utils import UUIDType
from marshmallow import Schema, fields
from . import db
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class EventType(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'event_types'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    type = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)

class EventTypeSchema(Schema):
    id = fields.Str(dump_only=True)
    type = fields.Str(required=True)
    color = fields.Str(required=True, load_only=True)
