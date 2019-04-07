from flask import Blueprint
from src.util import SchoolarApi

from src.controllers import FacultyResource, FacultyListResource


FACULTY_BLUEPRINT = Blueprint('faculty', __name__)

SchoolarApi(FACULTY_BLUEPRINT).add_resource(
    FacultyListResource,
    '/faculties'
)

SchoolarApi(FACULTY_BLUEPRINT).add_resource(
    FacultyResource,
    '/faculties/<string:id>'
)
