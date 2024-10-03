# # server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db, Earthquake  # Make sure Earthquake is imported from your models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


# Route to fetch earthquake by ID
@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    earthquake = Earthquake.query.get(id)

    if earthquake:
        response_body = {
            "id": earthquake.id,
            "location": earthquake.location,
            "magnitude": earthquake.magnitude,
            "year": earthquake.year
        }
        return make_response(jsonify(response_body), 200)
    else:
        response_body = {
            "message": f"Earthquake {id} not found."
        }
        return make_response(jsonify(response_body), 404)


# New route to fetch earthquakes based on magnitude
@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    # Query earthquakes with magnitude greater than or equal to the specified value
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # Prepare the response body with count and list of earthquakes
    quake_list = [{
        "id": quake.id,
        "location": quake.location,
        "magnitude": quake.magnitude,
        "year": quake.year
    } for quake in earthquakes]

    response_body = {
        "count": len(quake_list),
        "quakes": quake_list
    }

    return make_response(jsonify(response_body), 200)


if __name__ == '__main__':
    app.run(debug=True)
