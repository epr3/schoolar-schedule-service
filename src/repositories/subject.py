from src.models import Subject


class SubjectRepository:
  @staticmethod
  def get(id):
    return Subject.query.get_or_404(id)

  @staticmethod
  def get_all():
    return Subject.query.all()

  def update(id, **kwargs):
    subject = Subject.query.get(id)
    subject.update(**kwargs)
    return subject.save()

  def delete(id):
    subject = Subject.query.get(id)
    return subject.delete()

  @staticmethod
  def create(**kwargs):
    subject = Subject(**kwargs)
    return subject.save()
