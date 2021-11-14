# Python modules

from flask import Flask, jsonify
from flask.globals import request
import config
import os
import decimal
from urllib.request import urlopen 
import pandas as pd
import openpyxl
from openpyxl_image_loader import SheetImageLoader
from flask_pymongo import PyMongo

# Flask modules
from flask import render_template, json
# Api modules
from api import *

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# create a flask app
app = Flask(__name__)

app.config.update(
    DEBUG=config.DEBUG,
    SECRET_KEY=config.SECRET_KEY,
    MONGO_URI=config.MONGO_URI)
# mongo = PyMongo(app)
# db = mongo.db

# display index page
@app.route('/')
def index():
    # historyCollection = db.tradehistory
    # data = get_historical_trades("BTCUSDT", 3, "333")
    # data.set_index("id", inplace=True)
    # symbol = "BTCUSDT"
    # limit = 3
    # fromId = "333"
    # historyCollection.insert({"symbol": symbol, "limit": limit, "fromId": fromId, "data": data.to_dict('records')})

    # sell_result = historyCollection.find_one({"symbol": "BTCUSDT"})
    # print(sell_result)

    return render_template("index.html")
