from . import db, ma
from uuid import uuid4


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.String, primary_key=True, default=uuid4)
    room = db.Column(db.String, nullable=False)
    rrule = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    is_notifiable = db.Column(db.Boolean, default=False)
    subject_id = db.Column(db.String, db.ForeignKey(
        'subjects.id', ondelete='CASCADE'), nullable=False)
    subject = db.relationship(
        'Subject', backref=db.backref('event_subjects', lazy='dynamic'), foreign_keys=[subject_id])
    group_id = db.Column(db.String, db.ForeignKey(
        'groups.id', ondelete='CASCADE'), nullable=False)
    group = db.relationship(
        'Group', backref=db.backref('event_groups', lazy='dynamic'), foreign_keys=[group_id])
    professor_id = db.Column(db.String, nullable=False)

    def __init__(self, event, group_id, subject_id):
        self.event = event
        self.group_id = group_id
        self.subject_id = subject_id


class EventSchema(ma.ModelSchema):
    class Meta:
        model = Event
