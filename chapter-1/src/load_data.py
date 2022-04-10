# Import necessary modules
import pandas as pd
import numpy as np
import os
from IPython.core.display import display
from glob import glob

# Change directory
os.chdir('../')
# Enable dynamic loading to a file.

__dir__ = os.getcwd()

# Define get_data funciton to pull data


def get_data(file_name, master=False):
    if master == True:
        master_data = pd.read_csv(
            filepath_or_buffer=f'{__dir__}/data/{str(file_name)}', delimiter='\t', encoding='shift-jis')
        return master_data
    else:
        column_master_data = pd.read_csv(
            filepath_or_buffer=f'{__dir__}/data/{str("mst_column_name.txt")}', delimiter='\t', encoding='shift-jis')
        columns = column_master_data.column_name_en
        data = pd.read_csv(
            filepath_or_buffer=f'{__dir__}/data/{str(file_name)}', encoding='shift-jis', header=None)
        data.columns = columns
        return data


# Try using glob to get all data starting with diff
diff_files = glob(f'{__dir__}/data/{str("diff*.csv")}')
diff_files

# Concatenate diff data interractively
mst = pd.read_csv(
    filepath_or_buffer=f'{__dir__}/data/{str("mst_column_name.txt")}', delimiter='\t', encoding='shift-jis')
mst_columns = mst.column_name_en
data_0 = pd.read_csv(diff_files[0], encoding='shift-jis', header=None)
data_0.columns = mst_columns
data_1 = pd.read_csv(diff_files[1], encoding='shift-jis', header=None)
data_1.columns = mst_columns
data_concat = pd.concat([data_0, data_1])
data_concat.head()

# Turn concatenation process into function


pd.DataFrame(columns=pd.read_csv(
    diff_files[0], encoding='shift-jis', header=None).columns.tolist())


def get_diff_data(file_name, diff_file=True):
    # get column names from master data
    column_master_data = pd.read_csv(
        filepath_or_buffer=f'{__dir__}/data/{str("mst_column_name.txt")}', delimiter='\t', encoding='shift-jis')
    columns = column_master_data.column_name_en
    if diff_file == True:
        # get list of data using regular expression
        data_list = glob(f'{__dir__}/data/{str(file_name)}')
        # create a base dataframe that will be appended over loops
        column_base = pd.read_csv(
            data_list[0], encoding='shift-jis', header=None).columns.tolist()
        data = pd.DataFrame(columns=column_base)
        for i in data_list:
            data = data.append(pd.read_csv(
                i, encoding='shift-jis', header=None))
        data.columns = columns
        return data
    else:
        return column_master_data


# Testing my code
if __name__ == '__main__':

    # Read header data
    mst = get_data(file_name='mst_column_name.txt', master=True)
    print('Return Master data')
    display(mst.head(3))

    # Read all shizuoka data
    data = get_data(file_name='22_shizuoka_all_20210331.csv', master=False)
    print('Return Data after Renaming Column')
    display(data.head(3))

    # Read all diff data
    diff_data = get_diff_data(file_name="diff*.csv", diff_file=True)
    print('Iteration Data Test')
    display(diff_data.head(3))
