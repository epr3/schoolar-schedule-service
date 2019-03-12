from flask_script import Command
from seeder import ResolvingSeeder
from models import db

class Seeder(Command):
  def run(self):
    seeder = ResolvingSeeder(db.session)
    #course_entities = seeder.load_entities_from_yaml_file(
    #'./course.yaml', commit=True)
    faculty_entities = seeder.load_entities_from_yaml_file(
    './src/fixtures/faculty.yaml', commit=True)
    #group_entities = seeder.load_entities_from_yaml_file(
    #'./group.yaml', commit=True)
    #subject_entities = seeder.load_entities_from_yaml_file(
    #'./subject.yaml', commit=True)
    #event_entitities = seeder.load_entities_from_yaml_file(
    #'./event.yaml', commit=True)
