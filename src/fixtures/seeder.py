import json
import config
from flask import current_app
from flask_script import Command
from repositories import FacultyRepository

class Seeder(Command):
  def run(self):
    current_app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
    with open('./src/fixtures/faculty.json') as f:
      data = json.load(f)

    for item in data:
      FacultyRepository.create(**item)
