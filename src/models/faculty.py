from . import db, ma
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class Faculty(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'faculties'
    id = db.Column(db.String, primary_key=True, default=str(uuid4()))
    name = db.Column(db.String, nullable=False)


class FacultySchema(ma.ModelSchema):
    class Meta:
        model = Faculty
