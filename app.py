# Hello, Web

# This activity allows students to practice setting up a server and defining basic routes with Flask.

## Instructions

# Create an `app.py`, and make the necessary imports.

from flask import Flask, jsonify
import pandas as pd
import climate_analysis.ipynb

app = Flask(__name__)

routes = [(app.url_map)]

@app.route("/")
def index():
    return print(routes)

@app.route("/api/v1.0/precipitation")
def precip():
    precip_dict = precip_df.to_dict('list')
    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    return print("Test")

@app.route("/api/v1.0/tobs")
def tobs():
    return print("Test")

@app.route("/api/v1.0/<start>")
def start():
    return print("Test")

@app.route("/api/v1.0/<start>/<end>")
def duration():
    return print("Test")


from app import app

if __name__ == "__main__":
    app.run(debug=True)
