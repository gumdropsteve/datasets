import pandas as pd
import dask.delayed
from dask import compute


@dask.delayed
def make_smaller_csvs(big_csv, n_smaller_csvs=30, output_dir=''):

    len_df = 2985217
    smaller_len = int(len_df / n_smaller_csvs)
    fn = big_csv.split('.cs')[0]

    for i in range(n_smaller_csvs):
        if i == 0:
            end = smaller_len
            pd.read_csv(big_csv, nrows=end).to_csv(f'{output_dir}{fn}_part_{i}.csv', index=False)
        elif i == n_smaller_csvs - 1:
            start = i * smaller_len
            pd.read_csv(big_csv, skiprows=start).to_csv(f'{output_dir}{fn}_part_{i}.csv', index=False)
        else:
            start = i * smaller_len
            end = smaller_len
            pd.read_csv(big_csv, skiprows=start, nrows=end).to_csv(f'{output_dir}{fn}_part_{i}.csv', index=False)

    print(f'{big_csv} done')


if __name__=='__main__':
    a = dask.delayed(make_smaller_csvs)('properties_2016.csv')
    b = dask.delayed(make_smaller_csvs)('properties_2017.csv')
    compute(*[a, b])
