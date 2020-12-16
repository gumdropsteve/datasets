# datasets

## **Airlines**
#### Python
```python
import os
from urllib.request import urlretrieve

data_dir = 'data/'
base_url = 'https://github.com/gumdropsteve/datasets/raw/master/'
file_name = 'airlines.parquet'

# create data dir if doesn't exist
if not os.path.exists(data_dir):
    os.system('mkdir data')

# download file if not found in data dir
if not os.path.isfile(data_dir + file_name):
    print(f'Downloading {base_url + file_name} to {data_dir + file_name}')
    urlretrieve(base_url + file_name, data_dir + file_name)
    print('Done')
else:
    print(f'{file_name} already downloaded')
```

## **Blobs**
#### Python
```python
try:
  import cudf
except:
  import pandas as cudf

cudf.read_csv('https://raw.githubusercontent.com/gumdropsteve/datasets/master/blobs.csv')
```

#### R
```r
link <- 'https://raw.githubusercontent.com/gumdropsteve/datasets/master/blobs.csv'
df <- read.csv(link)
```

## **Dog or Horse**
#### Python
```python
try:
  import cudf
except:
  import pandas as cudf

df = cudf.read_csv('https://raw.githubusercontent.com/gumdropsteve/datasets/master/dog_or_horse.csv')
```

#### R
```r
link <- 'https://raw.githubusercontent.com/gumdropsteve/datasets/master/dog_or_horse.csv'
df <- read.csv(link)
```

## **Iris**
#### Python
```python
try:
  import cudf
except:
  import pandas as cudf

cudf.read_csv('https://raw.githubusercontent.com/gumdropsteve/datasets/master/iris.csv')
```

#### R
```r
link <- 'https://raw.githubusercontent.com/gumdropsteve/datasets/master/iris.csv'
df <- read.csv(link)
```

## **NYC Taxi**
#### Python
```python
import pandas as pd

# 2009 - 2016
for year in range(2009, 2017):
    # january - december
    for month in range(1, 13):
        # correct single digit months
        if month < 10:
            month = f'0{month}'
        # initial df (january 2009)
        if (year==2009) and (month=='01'):
            df = pd.read_parquet(f'https://github.com/gumdropsteve/datasets/raw/master/nyc_taxi/yellow_tripdata_{year}-{month}.parquet')
        # february 2009 - june 2016
        elif (year < 2016) or (int(month) < 7):
            # add on to existing df
            df = pd.concat([df, pd.read_parquet(f'https://github.com/gumdropsteve/datasets/raw/master/nyc_taxi/yellow_tripdata_{year}-{month}.parquet')])
df
```

## **NYC Transport**
#### Python
Add this snippet to the below based on which parts of the NYC Transport dataset you want to download.
```python
import os
import urllib

# tag data dir & sub dirs
data_dir = 'raw_data/'
taxi_sub_dir = 'taxi/'
uber_sub_dir = 'uber/'
t_zones_sub_dir = 'zones/'

# create directories if they don't exist
for d in [data_dir, f'{data_dir}/{taxi_sub_dir}', f'{data_dir}/{uber_sub_dir}', f'{data_dir}/{t_zones_sub_dir}']:
    if not os.path.exists(d):
        os.system(f'mkdir {d}')
        
# (raw) url to directory we're downloading
base_url = 'https://raw.githubusercontent.com/gumdropsteve/datasets/master/nyc_transport/'
```

### Green Taxi
#### Python
```python
for file in [f'green_tripdata_{f}.csv' for f in ['2013-08', '2014-01', '2015-01', '2016-01', '2017-01', '2018-01', '2019-01']]:
    if not os.path.isfile(data_dir + taxi_sub_dir + file):
        print(f'Downloading {base_url + taxi_sub_dir + file} to {data_dir + taxi_sub_dir + file}')
        urllib.request.urlretrieve(base_url + taxi_sub_dir + file, data_dir + taxi_sub_dir + file)
```

### Yellow Taxi
#### Python
```python
for file in [f'yellow_tripdata_20{f}-01.csv' for f in ['09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]:
    if not os.path.isfile(data_dir + taxi_sub_dir + file):
        print(f'Downloading {base_url + taxi_sub_dir + file} to {data_dir + taxi_sub_dir + file}')
        urllib.request.urlretrieve(base_url + taxi_sub_dir + file, data_dir + taxi_sub_dir + file)
```

### Uber
#### Python
```python
# 2014
for file in [f'uber-raw-data-{month}14.csv' for month in ['apr', 'aug', 'jul', 'jun', 'may', 'sep']]:
    if not os.path.isfile(data_dir + uber_sub_dir + file):
        print(f'Downloading {base_url + uber_sub_dir + file} to {data_dir + uber_sub_dir + file}')
        urllib.request.urlretrieve(base_url + uber_sub_dir + file, data_dir + uber_sub_dir + file)
        
# 2015
file = 'uber-raw-data-janjune-15.csv'
if not os.path.isfile(data_dir + uber_sub_dir + file):
    print(f'Downloading {base_url + uber_sub_dir + file} to {data_dir + uber_sub_dir + file}')
    urllib.request.urlretrieve(base_url + uber_sub_dir + file, data_dir + uber_sub_dir + file)
```

### Taxi Zones (CUDA Shapefiles)
#### Python
```python
for file in [f'cu_taxi_zones.{f}' for f in ['cpg', 'dbf', 'prj', 'shp', 'shx']]:
    if not os.path.isfile(data_dir + t_zones_sub_dir + file):
        print(f'Downloading {base_url + t_zones_sub_dir + file} to {data_dir + t_zones_sub_dir + file}')
        urllib.request.urlretrieve(base_url + t_zones_sub_dir + file, data_dir + t_zones_sub_dir + file)
```

## **Yellow Cab Averages**
#### Python
```python
import pandas as pd

pd.read_csv('https://raw.githubusercontent.com/gumdropsteve/datasets/master/yellow_cab_ymd_averages.csv')
```

#### R
```r
link <- 'https://raw.githubusercontent.com/gumdropsteve/datasets/master/yellow_cab_ymd_averages.csv'
df <- read.csv(link)
```
