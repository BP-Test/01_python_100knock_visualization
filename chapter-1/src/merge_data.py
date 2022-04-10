# Import necessary modules
import pandas as pd
import numpy as np
import os
from IPython.core.display import display
from glob import glob
from load_data import get_data
# Change directory
os.chdir('../')
# Enable dynamic loading to a file.

__dir__ = os.getcwd()

# Process
0. load base csv file
data_base = pd.read_csv(f'{__dir__}/data/22_shizuoka_all_20210331.csv',encoding='shift-jis',header=None)
data)ba

1. Load all the master data using globe
master_data_list = glob(f'{__dir__}/data/{str("mst*.csv")}',encoding='shift-jis')
2. merge dataframe

3. Turn into iteration
for i in master_data_list:
    key_column = i.columns.toliist()[0]
    data = pd.merge(fact_data, i, on=key_column, validate='m:1')
data = data.
return data
4. return result


def merge_data(fact_data, file_name, diff_file=True):

    # get column names from master data
    column_master_data = pd.read_csv(
        filepath_or_buffer=f'{__dir__}/data/{str("mst_column_name.txt")}', delimiter='\t', encoding='shift-jis', dtype='object')
    columns = column_master_data.column_name_en
    if diff_file == True:
        # get list of data using regular expression
        data_list = glob(f'{__dir__}/data/{str(file_name)}')
        # create a base dataframe that will be appended over loops
        column_base = pd.read_csv(
            data_list[0], encoding='shift-jis', header=None, dtype='object').columns.tolist()
        data = pd.DataFrame(columns=column_base, dtype='object')
        for i in data_list:
            data = data.append(pd.read_csv(
                i, encoding='shift-jis', header=None))
        data.columns = columns
        data = data.astype(str).replace('nan',np.nan)
        return data
    else:
        return column_master_data


# Testing my code
if __name__ == '__main__':
    # Read all diff data
    diff_data = get_diff_data(file_name="diff*.csv", diff_file=True)
    print('Iteration Data Test')
    display(diff_data.head(3))
    display(diff_data.info(verbose=True))
