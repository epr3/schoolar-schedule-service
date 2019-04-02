from flask import Blueprint
from flask_restful import Api

from src.controllers import FacultyResource, FacultyListResource


FACULTY_BLUEPRINT = Blueprint('faculty', __name__)

Api(FACULTY_BLUEPRINT).add_resource(
    FacultyListResource,
    '/faculties'
)

Api(FACULTY_BLUEPRINT).add_resource(
    FacultyResource,
    '/faculties/<string:id>'
)
