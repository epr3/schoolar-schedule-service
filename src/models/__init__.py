from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .faculty import Faculty, FacultySchema
from .subject import Subject, SubjectSchema
from .course import Course, CourseSchema
from .group import Group, GroupSchema
from .event import Event, EventSchema
