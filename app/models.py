from . import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    notes = db.Column(db.Text)

    def __init__(self, latitude, longitude, notes):
        self.latitude = latitude
        self.longitude = longitude
        self.notes = notes

    def __repr__(self):
        return '<Location %s, %s>' % (self.latitude, self.longitude)

    def serialize(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'notes': self.notes,
        }

