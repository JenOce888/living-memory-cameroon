# Model: Person (the elder being interviewed)
from . import db
from datetime import date

class Person(db.Model):
    __tablename__ = 'persons'

    id               = db.Column(db.Integer, primary_key=True)
    last_name        = db.Column(db.String(100), nullable=False)
    first_name       = db.Column(db.String(100))
    approx_age       = db.Column(db.Integer)
    ethnic_group     = db.Column(db.String(100))
    region           = db.Column(db.String(100))
    city_village     = db.Column(db.String(100))
    native_language  = db.Column(db.String(100))
    consent_given    = db.Column(db.Boolean, default=False)
    interview_date   = db.Column(db.Date, default=date.today)

    # One person can give many testimonies and share many plant usages
    testimonies      = db.relationship('Testimony',      backref='person', lazy=True)
    oral_histories   = db.relationship('OralHistory',    backref='person', lazy=True)
    plant_usages     = db.relationship('MedicinalUsage', backref='person', lazy=True)

    def to_dict(self):
        return {
            'id':              self.id,
            'last_name':       self.last_name,
            'first_name':      self.first_name,
            'approx_age':      self.approx_age,
            'ethnic_group':    self.ethnic_group,
            'region':          self.region,
            'city_village':    self.city_village,
            'native_language': self.native_language,
            'consent_given':   self.consent_given,
            'interview_date':  str(self.interview_date),
        }
