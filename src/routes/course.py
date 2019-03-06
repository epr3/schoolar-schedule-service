from flask import Blueprint
from flask_restful import Api

from controllers import CourseResource, CourseListResource


COURSE_BLUEPRINT = Blueprint('course', __name__)

Api(COURSE_BLUEPRINT).add_resource(
    CourseListResource,
    '/courses'
)

Api(COURSE_BLUEPRINT).add_resource(
    CourseResource,
    '/courses/<string:id>'
)
