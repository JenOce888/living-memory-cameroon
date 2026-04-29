# Model: Plant (a medicinal plant known by the elder)
from . import db

class Plant(db.Model):
    __tablename__ = 'plants'

    id                  = db.Column(db.Integer, primary_key=True)
    local_name          = db.Column(db.String(200), nullable=False)  # name in local language
    french_name         = db.Column(db.String(200))
    scientific_name     = db.Column(db.String(200))
    botanical_family    = db.Column(db.String(100))
    usage_region        = db.Column(db.String(100))
    part_used           = db.Column(db.String(200))   # leaves, roots, bark, seeds...
    photo_url           = db.Column(db.String(500))   # photo on Cloudinary
    description         = db.Column(db.Text)

    # One plant can have many medicinal usages described by different people
    usages = db.relationship('MedicinalUsage', backref='plant', lazy=True)

    def to_dict(self):
        return {
            'id':               self.id,
            'local_name':       self.local_name,
            'french_name':      self.french_name,
            'scientific_name':  self.scientific_name,
            'usage_region':     self.usage_region,
            'part_used':        self.part_used,
            'photo_url':        self.photo_url,
            'description':      self.description,
        }
