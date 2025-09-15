# Parcels Time Series Dataset

## Overview

This dataset contains time series data for spatial parcels, split across 11 files for efficient processing. The data appears to track visitation or activity patterns across different spatial coordinates over time.

## Dataset Structure

### Files
- **Format**: 29 CSV files (`output_part_1.csv` through `output_part_11.csv`)
- **Records per file**: 3,500 rows
- **Total estimated records**: 110,000 rows
- **File encoding**: UTF-8

### Schema

| Column | Type | Description |
|--------|------|-------------|
| `name` | String | Entity identifier (all records contain "parcels") |
| `tags` | String | Spatial coordinates in dictionary format: `{'x': 'value', 'y': 'value'}` |
| `data_cols` | String | Column definitions for time series data: `['time', 'first']` |
| `data_visits` | String | Time series data as nested arrays: `[[timestamp, value], ...]` |

## Data Characteristics

### Spatial Coverage
- **Coordinate system**: Grid-based with integer coordinates
- **X-axis range**: Starting from -1 (continues in other files)
- **Y-axis range**: Negative values from -1 to approximately -107+ 
- **Coordinate pattern**: Sequential progression through grid cells

### Temporal Coverage
- **Time period**: March 2021 onwards (based on sample: 2021-03-30)
- **Timestamp format**: Unix milliseconds (13 digits)
- **Data frequency**: Variable intervals between measurements
- **Value type**: Integer counts (appears to track visit frequency or activity levels)

### Data Format Details
- **tags**: Stored as string representation of Python dictionary
- **data_cols**: Defines time series structure - consistently `['time', 'first']`
- **data_visits**: Arrays of [timestamp, count] pairs stored as strings

## Use Cases

This dataset is suitable for:
- **Spatial-temporal analysis**: Understanding activity patterns across geographic locations
- **Time series forecasting**: Predicting future activity at specific coordinates
- **Hotspot detection**: Identifying high-activity areas and temporal patterns
- **Mobility analytics**: Analyzing movement and visitation patterns
- **Geographic information systems (GIS)**: Spatial data visualization and analysis

## Data Quality

- **Completeness**: All records contain data in all four columns
- **Consistency**: Uniform naming convention ("parcels") and data structure
- **Format**: Well-structured with predictable patterns
- **Size**: Large dataset suitable for machine learning and statistical analysis

## Technical Notes

- **Processing**: Consider using streaming or chunked processing for the full 110k records
- **Parsing**: The `tags` and `data_visits` columns require string parsing to extract structured data
- **Memory**: Each record contains variable-length time series data; memory usage may vary significantly
- **Timestamps**: Convert Unix milliseconds to datetime objects for temporal analysis

## Getting Started

```python
import pandas as pd
import ast

# Load a single file
df = pd.read_csv('output_part_1.csv')

# Parse coordinate tags
df['coordinates'] = df['tags'].apply(lambda x: ast.literal_eval(x))
df['x'] = df['coordinates'].apply(lambda coord: int(coord['x']))
df['y'] = df['coordinates'].apply(lambda coord: int(coord['y']))

# Parse time series data
df['visits_data'] = df['data_visits'].apply(lambda x: ast.literal_eval(x))
```

## File Organization

```
dataset/
├── output_part_1.csv   # Rows 1-3,500
├── output_part_2.csv   # Rows 3,501-7,000
├── output_part_3.csv   # Rows 7,001-10,500
├── ...
├── output_part_28.csv  # Rows 94,501-98,000
└── output_part_29.csv  # Rows 98,001-101,222
```