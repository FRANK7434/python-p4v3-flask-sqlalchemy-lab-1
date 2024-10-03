from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Metadata setup
metadata = MetaData()

# Initialize the database with the metadata
db = SQLAlchemy(metadata=metadata)

# Define the Earthquake model
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'  # table name

    id = db.Column(db.Integer, primary_key=True)  # primary key column
    magnitude = db.Column(db.Float, nullable=False)  # magnitude column (float)
    location = db.Column(db.String, nullable=False)  # location column (string)
    year = db.Column(db.Integer, nullable=False)  # year column (integer)

    # String representation method
    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
