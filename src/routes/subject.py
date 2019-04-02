from flask import Blueprint
from flask_restful import Api

from src.controllers import SubjectResource, SubjectListResource


SUBJECT_BLUEPRINT = Blueprint('subject', __name__)

Api(SUBJECT_BLUEPRINT).add_resource(
    SubjectListResource,
    '/subjects'
)

Api(SUBJECT_BLUEPRINT).add_resource(
    SubjectResource,
    '/subjects/<string:id>'
)
