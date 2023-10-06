These files represent historical stock and commodity data by day.

Similar datasets can be pulled from the Yahoo! Finance API like so;


import yfinance as yf

# pull BTC historical market data
btc_hist = yf.Ticker('BTC-USD').history(period="max", auto_adjust=True)
