# NYC-Transport Sample Dataset
Samples of raw CSV files for NYC-Transport.

`taxi/`
- Green (2013-2019) & Yellow (2009-2019) taxi rides 
- 100,000 rows per file, 1 file per year (18 files total)
  - Total Green rows = 607,623
  - Total Yellow rows = 1,100,000
- NOTE: `green_tripdata_2013-08.csv` has only 7,623 rows

`uber/`
- Uber (2014-2015) rides
- 100,000 rows per file, 6 files for 2014, 1 file for 2015 (7 files total)
    - Total 2014 rows = 600,000
    - Total 2015 rows = 100,000
- NOTE: 2014 data is overrepresented.

`zones/`
- NYC taxi zones shapefile(s) for cuspatial.