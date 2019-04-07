from flask import Blueprint
from src.util import SchoolarApi

from src.controllers import CourseResource, CourseListResource


COURSE_BLUEPRINT = Blueprint('course', __name__)

SchoolarApi(COURSE_BLUEPRINT).add_resource(
    CourseListResource,
    '/courses'
)

SchoolarApi(COURSE_BLUEPRINT).add_resource(
    CourseResource,
    '/courses/<string:id>'
)
