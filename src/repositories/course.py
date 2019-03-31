from models import Course


class CourseRepository:
  @staticmethod
  def get(id):
    return Course.query.get_or_404(id)

  @staticmethod
  def get_all():
    return Course.query.all()

  def update(id, **kwargs):
    course = Course.query.get(id)
    course.update(**kwargs)
    return course.save()

  def delete(id):
    course = Course.query.get(id)
    return course.delete()

  @staticmethod
  def create(**kwargs):
    course = Course(**kwargs)
    return course.save()
