from src.models import Faculty


class FacultyRepository:
  @staticmethod
  def get(id):
    return Faculty.query.get_or_404(id)

  @staticmethod
  def get_all():
    return Faculty.query.all()

  def update(id, **kwargs):
    faculty = Faculty.query.get(id)
    faculty.update(**kwargs)
    return faculty.save()

  def delete(id):
    faculty = Faculty.query.get(id)
    return faculty.delete()

  @staticmethod
  def create(**kwargs):
    faculty = Faculty(**kwargs)
    return faculty.save()
