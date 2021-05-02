from flask import Flask
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello world'

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)
app = Flask(__name__)
# Define the Welcome route
@app.route("/")

def welcome():
    return(
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        ''')
 

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= prev_year).all()
    # Unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# Define the function and specify a start and end date for the range
def stats(start=None, end=None):
    # Create a query to select the minimum, average, and maximum temperatures from our SQLite database.
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # Determine the starting and ending dates
    if not end:
        # Query the database using the list "sel"
        # Asterisk shows there will be multiple results for our query: minimum, average, and maximum temperatures
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
                filter(Measurement.date <= end).all()
        # Unravel the results into a one-dimensional array and convert them to a list
        temps = list(np.ravel(results))
        return jsonify(temps)

    # To get the statistics data
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Run the code
if __name__ == '__main__':
    app.run()



