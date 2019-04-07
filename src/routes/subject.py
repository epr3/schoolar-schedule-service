from flask import Blueprint
from src.util import SchoolarApi

from src.controllers import SubjectResource, SubjectListResource


SUBJECT_BLUEPRINT = Blueprint('subject', __name__)

SchoolarApi(SUBJECT_BLUEPRINT).add_resource(
    SubjectListResource,
    '/subjects'
)

SchoolarApi(SUBJECT_BLUEPRINT).add_resource(
    SubjectResource,
    '/subjects/<string:id>'
)
