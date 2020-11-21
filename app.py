# Hello, Web

# This activity allows students to practice setting up a server and defining basic routes with Flask.

## Instructions

# Create an `app.py`, and make the necessary imports.

from flask import Flask, jsonify, url_for
import pandas as pd

from ipynb.fs.full.climate_analysis import *

app = Flask(__name__)

from app import app

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

links = []
for rule in app.url_map.iter_rules():
    if "GET" in rule.methods and has_no_empty_params(rule):
        url = url_for(rule.endpoint, **(rule.defaults or {}))
        links.append((url, rule.endpoint))


@app.route("/")
def index():
    return print(links)

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




if __name__ == "__main__":
    app.run(debug=True)
