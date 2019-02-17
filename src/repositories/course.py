from models import Course, CourseSchema

course_schema = CourseSchema()

class CourseRepository:
  @staticmethod
  def get(id):
    return course_schema.jsonify(Course.get(id))

  @staticmethod
  def get_all():
    return course_schema.jsonify(Course.all())

  def update(id, **kwargs):
    course = self.get(id)
    course.update(**kwargs)
    return course.save()

  def delete(id):
    course = self.get(id)
    return course.delete()
