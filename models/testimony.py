# Model: Testimony (what the elder says about a historical event)
from . import db
from datetime import date

class Testimony(db.Model):
    __tablename__ = 'testimonies'

    id                  = db.Column(db.Integer, primary_key=True)
    person_id           = db.Column(db.Integer, db.ForeignKey('persons.id'), nullable=False)
    title               = db.Column(db.String(200), nullable=False)
    transcription       = db.Column(db.Text)           # written text of what they said
    audio_url           = db.Column(db.String(500))    # link to audio file on Cloudinary
    video_url           = db.Column(db.String(500))    # link to video file on Cloudinary
    historical_period   = db.Column(db.String(100))
    related_event       = db.Column(db.String(200))
    testimony_language  = db.Column(db.String(100))
    record_date         = db.Column(db.Date, default=date.today)

    def to_dict(self):
        return {
            'id':                 self.id,
            'person_id':          self.person_id,
            'title':              self.title,
            'transcription':      self.transcription,
            'audio_url':          self.audio_url,
            'video_url':          self.video_url,
            'historical_period':  self.historical_period,
            'related_event':      self.related_event,
            'testimony_language': self.testimony_language,
            'record_date':        str(self.record_date),
        }
