# Model: MedicinalUsage (links a plant to a person + describes how they use it)
from . import db

class MedicinalUsage(db.Model):
    __tablename__ = 'medicinal_usages'

    id               = db.Column(db.Integer, primary_key=True)
    plant_id         = db.Column(db.Integer, db.ForeignKey('plants.id'),   nullable=False)
    person_id        = db.Column(db.Integer, db.ForeignKey('persons.id'),  nullable=False)
    disease_treated  = db.Column(db.String(200))   # what illness does it treat?
    preparation      = db.Column(db.Text)           # how to prepare the remedy
    cultural_context = db.Column(db.Text)           # rituals, beliefs, seasons involved
    precautions      = db.Column(db.Text)           # warnings / side effects

    def to_dict(self):
        return {
            'id':               self.id,
            'plant_id':         self.plant_id,
            'person_id':        self.person_id,
            'disease_treated':  self.disease_treated,
            'preparation':      self.preparation,
            'cultural_context': self.cultural_context,
            'precautions':      self.precautions,
        }
