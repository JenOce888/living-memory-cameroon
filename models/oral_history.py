# Model: OralHistory (myths, legends, proverbs, traditions passed down orally)
# This is different from a testimony: it is NOT about a personal lived experience,
# but about stories, proverbs, or cultural knowledge the elder knows.
from . import db
from datetime import date

CATEGORY_CHOICES = ['myth', 'legend', 'proverb', 'folktale', 'tradition', 'other']

class OralHistory(db.Model):
    __tablename__ = 'oral_histories'

    id              = db.Column(db.Integer, primary_key=True)
    person_id       = db.Column(db.Integer, db.ForeignKey('persons.id'), nullable=False)

    # What kind of oral tradition is this?
    category        = db.Column(db.String(50))   # myth / legend / proverb / folktale / tradition

    title           = db.Column(db.String(200), nullable=False)
    original_text   = db.Column(db.Text)         # the story/proverb in the original language
    translation_fr  = db.Column(db.Text)         # French translation
    context         = db.Column(db.Text)         # when/why is this told? what does it teach?
    ethnic_group    = db.Column(db.String(100))
    region          = db.Column(db.String(100))
    language        = db.Column(db.String(100))
    audio_url       = db.Column(db.String(500))  # audio recording of the elder telling it
    record_date     = db.Column(db.Date, default=date.today)

    def to_dict(self):
        return {
            'id':             self.id,
            'person_id':      self.person_id,
            'category':       self.category,
            'title':          self.title,
            'original_text':  self.original_text,
            'translation_fr': self.translation_fr,
            'context':        self.context,
            'ethnic_group':   self.ethnic_group,
            'region':         self.region,
            'language':       self.language,
            'audio_url':      self.audio_url,
            'record_date':    str(self.record_date),
        }
