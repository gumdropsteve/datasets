These files represent historical stock and commodity data by day.

## Access data with Pandas
You can pull these datasets straight into a Pandas DataFrame by following this format, changing the `file` name to whichever file from this folder that you wish to read;
```py
import pandas as pd

file = "BTC.csv"

raw_data_url = "https://raw.githubusercontent.com/gumdropsteve/datasets/dataset/stocks/README/stocks"

btc_hist = pd.read_csv(f"{raw_data_url}/{file}")
```

#### Live Data
Similar datasets to those found in this folder, with live data, can be pulled from the Yahoo! Finance API like so;
```py
# !pip install yfinance
import yfinance as yf

btc_hist = yf.Ticker('BTC-USD').history(period="max", auto_adjust=True)
```
