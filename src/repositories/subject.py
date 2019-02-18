from flask import jsonify
from models import Subject, SubjectSchema

subject_schema = SubjectSchema()
subjects_schema = SubjectSchema(many=True)


class SubjectRepository:
  @staticmethod
  def get(id):
    return subject_schema.jsonify(Subject.query.get(id))

  @staticmethod
  def get_all():
    result = subjects_schema.dump(Subject.query.all())
    return jsonify(result.data)

  def update(id, **kwargs):
    subject = Subject.query.get(id)
    subject.update(**kwargs)
    return subject_schema.jsonify(subject.save())

  def delete(id):
    subject = Subject.query.get(id)
    return subject.delete()

  @staticmethod
  def create(**kwargs):
    subject = Subject(**kwargs)
    return subject_schema.jsonify(subject.save())
