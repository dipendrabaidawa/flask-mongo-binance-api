# Python modules

import os
import config
# Flask modules
from flask import Flask
from flask.globals import request
from flask import render_template
from flask_pymongo import PyMongo

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
mongo = PyMongo(app)
db = mongo.db

# display index page
@app.route('/',methods = ['GET', 'POST'])
def index():
    # Get DB Collection
    historyCollection = db.tradehistory

    # Default Parameters
    symbol = "BTCUSDT"
    limit = 10
    fromId = 1

    # Post Request
    if request.method == "POST":
        symbol = request.form.get('symbol')
        limit = int(request.form.get('limit'))
        fromId = int(request.form.get('fromId'))

    sell_history = []
    buy_history = []
    
    result = historyCollection.find({
        "$query": {
            "$and" : [
                {"id": {"$gte": fromId}},
                {"symbol": {"$eq": symbol}}
            ]
        },
        "$orderby": {
            "id": 1
        }
    }).limit(limit)

    exist_max_trade_id = 0
    for row in result:
        if exist_max_trade_id < row['id']:
            exist_max_trade_id = row['id']
        
        if row['isBuyerMaker'] == True:
            sell_history.append(row)
        else:
            buy_history.append(row)
    
    # in case which no exists in database, from exist_max_trade_id, fetching data from binance server
    
    if exist_max_trade_id < fromId + limit -1:
        not_enough_number = fromId + limit - exist_max_trade_id
        fromId_to_fetch = exist_max_trade_id + 1
        
        data = get_historical_trades(symbol, not_enough_number, fromId_to_fetch)
        data.index = [x for x in data.id]
        data = data.assign(symbol = symbol)
        historyCollection.insert(data.to_dict("records"))

        # append new fetched data to sell_history and buy_history dic
        for row in data.to_dict('records'):
            if row['isBuyerMaker'] == True:
                sell_history.append(row)
            else:
                buy_history.append(row)
    
    return render_template("index.html", \
        sell_history=sell_history, buy_history=buy_history)
