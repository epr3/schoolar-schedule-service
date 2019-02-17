from . import db, ma
from uuid import uuid4


class Faculty(db.Model):
    __tablename__ = 'faculties'
    id = db.Column(db.String, primary_key=True, default=uuid4)
    name = db.Column(db.String, nullable=False)

    def __init__(self, faculty):
        self.faculty = faculty


class FacultySchema(ma.ModelSchema):
    class Meta:
        model = Faculty
