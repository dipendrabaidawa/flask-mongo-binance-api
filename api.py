from binance.client import Client
import pandas as pd

API_KEY = "NuAA5EiCTvF60kGypKc5poB9FFNDJN95mysOzyRDpY9jlxDBzrZrASnCuc2pLl4T"
SECRET_KEY = "1C9FeBldP19YpG4t1J91uyOm5gBenWQ9swGsROISeNe4yu0KJF1Qb0V0xXdUjw8m"

client = Client(API_KEY, SECRET_KEY)

def get_historical_trades(symbol, limit, fromId):

    trades = client.get_historical_trades(symbol=symbol, limit=limit, fromId=fromId)
    df = pd.DataFrame(trades)
    
    return df

def get_all_symbols():
    symbols = client.get_exchange_info()
    return symbols