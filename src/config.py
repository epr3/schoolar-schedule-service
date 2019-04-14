import logging
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

DEBUG = os.environ.get('ENVIRONMENT') == 'DEV'
APPLICATION_ROOT = os.environ.get('APPLICATION_ROOT', '/application')
HOST = os.environ.get('APPLICATION_HOST')
PORT = int(os.environ.get('APPLICATION_PORT', '3000'))

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

# DB_CONTAINER = os.getenv('APPLICATION_DB_CONTAINER', 'db')
DB_URI = os.environ.get('APPLICATION_DB') or 'sqlite:///' + \
    os.path.join(basedir, 'app.db')

# logging.basicConfig(
#     filename=os.getenv('SERVICE_LOG', 'server.log'),
#     level=logging.DEBUG,
#     format='%(levelname)s: %(asctime)s \
#         pid:%(process)s module:%(module)s %(message)s',
#     datefmt='%d/%m/%y %H:%M:%S',
# )
