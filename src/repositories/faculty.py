from models import Faculty, FacultySchema

faculty_schema = FacultySchema()


class FacultyRepository:
  @staticmethod
  def get(id):
    return faculty_schema.jsonify(Faculty.query.get(id))

  @staticmethod
  def get_all():
    return faculty_schema.jsonify(Faculty.query.all())

  def update(id, **kwargs):
    faculty = Faculty.query.get(id)
    faculty.update(**kwargs)
    return faculty_schema.jsonify(faculty.save())

  def delete(id):
    faculty = Faculty.query.get(id)
    return faculty.delete()

  @staticmethod
  def create(**kwargs):
    faculty = Faculty(**kwargs)
    return faculty_schema.jsonify(faculty.save())
