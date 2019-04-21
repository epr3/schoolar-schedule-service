import click
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask.blueprints import Blueprint
from flask_jwt_extended import JWTManager

from . import config
from . import routes
from src.models import db

# config your API specs
# you can define multiple specs in the case your api has multiple versions
# ommit configs to get the default (all views exposed in /spec url)
# rule_filter is a callable that receives "Rule" object and
#   returns a boolean to filter in only desired views

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['JWT_HEADER_TYPE'] = 'JWT'
app.config['JWT_IDENTITY_CLAIM'] = 'sub'
app.config['SQLALCHEMY_ECHO'] = True
app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
db.init_app(app)
db.app = app

migrate = Migrate(app, db)

jwt = JWTManager(app)

@jwt.unauthorized_loader
def unauthorized_callback(reason):
    return 'Unauthorized', 401

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(
            blueprint
        )


@app.route('/healthz')
def healthz():
    return 'OK!'


@app.cli.command()
def test_command():
    click.echo('Test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
