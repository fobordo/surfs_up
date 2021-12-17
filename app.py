# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set up the database

# Allow access to and ability to query the SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to the SQLite database
session = Session(engine)

# Set up Flask
app = Flask(__name__)

# Create the welcome route (homepage)
@app.route('/')

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br>
    Available Routes:<br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/temp/start/end<br>
    ''')

# Create the precipitation route
@app.route("/api/v1.0/precipitation")

def precipitation():
    
    # Calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    
    # Get query results into a dictionary format
    precip = {date: prcp for date, prcp in precipitation}
    
    # Format query results into a JSON structured file
    return jsonify(precip)
        
# Create the stations route
@app.route("/api/v1.0/stations")

def stations():
    
    # Get all the stations in the database
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
 
# Create the monthly temperature route
@app.route("/api/v1.0/tobs")

def temp_monthly():
    
    # Calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    
    # Unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))
    
    # jsonify the list and return the results
    return jsonify(temps=temps)

# Create the statistics route
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    # Determine the starting and ending date
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    
    # Calculate the temperature minimum, average, and maximum with the start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)