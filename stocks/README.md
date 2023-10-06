These files represent historical stock and commodity data by day.

## Access data with Pandas
You can pull these datasets straight into a Pandas DataFrame by following this format;

import pandas as pd

file = "BTC.csv"

raw_data_url = "https://raw.githubusercontent.com/gumdropsteve/datasets/dataset/stocks/README/stocks"

btc_hist = pd.read_csv("{raw_data_url}/{file}")


#### Live Data
Similar datasets can be pulled from the Yahoo! Finance API like so;


import yfinance as yf

# pull BTC historical market data
btc_hist = yf.Ticker('BTC-USD').history(period="max", auto_adjust=True)
