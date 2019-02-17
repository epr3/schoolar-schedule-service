from . import db, ma
from .abstract import BaseModel, MetaBaseModel
from uuid import uuid4


class Faculty(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'faculties'
    id = db.Column(db.String, primary_key=True, default=uuid4)
    name = db.Column(db.String, nullable=False)

    def __init__(self, faculty):
        self.faculty = faculty


class FacultySchema(ma.ModelSchema):
    class Meta:
        model = Faculty
