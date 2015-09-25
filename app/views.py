from app import app, db
from models import Location
from flask import request, render_template
import json


@app.route('/', methods=['GET'])
def index():
    locations = [location.serialize() for location in Location.query.all()]
    locations = json.dumps(locations)
    return render_template('index.html', locations=locations)


@app.route('/health', methods=['GET'])
def health():
    return 'OK', 200


@app.route('/coordinates', methods=['POST'])
def coordinates():
    payload = request.get_json()
    for coordinate in payload['coordinates']:
        latitude, longitude, notes = coordinate['latitude'], \
                                     coordinate['longitude'], coordinate['notes']
        location = Location(latitude, longitude, notes)
        db.session.add(location)
    db.session.commit()
    return 'OK', 200

