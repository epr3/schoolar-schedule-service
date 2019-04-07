FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install pipenv

RUN pipenv install --pre -r requirements.txt

ADD . .

RUN pipenv run python manage.py db upgrade
