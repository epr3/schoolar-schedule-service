from flask import Flask
from flask.blueprints import Blueprint
from flask_migrate import Migrate, MigrateCommand

import config
from models import db, ma
import routes

# config your API specs
# you can define multiple specs in the case your api has multiple versions
# ommit configs to get the default (all views exposed in /spec url)
# rule_filter is a callable that receives "Rule" object and
#   returns a boolean to filter in only desired views

server = Flask(__name__)

server.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db.init_app(server)
ma.init_app(server)
db.app = server
ma.app = server

migrate = Migrate(server, db)

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint
        )


@server.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=3000, debug=True)
