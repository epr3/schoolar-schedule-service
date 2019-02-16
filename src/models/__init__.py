from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

from .course import Course, CourseSchema
from .event import Event, EventSchema
from .faculty import Faculty, FacultySchema
from .group import Group, GroupSchema
from .subject import Subject, SubjectSchema
