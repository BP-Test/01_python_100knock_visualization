# Import necessary modules
import pandas as pd
import numpy as np
import os
from IPython.core.display import display
from glob import glob
from pathlib import Path
# Change directory
os.chdir('../')
# Enable dynamic loading to a file.

__dir__ = os.getcwd()

# Define get_data funciton to pull data


def get_data(file_name, master=False):
    """Returns a dataframe having columns from master data

    Args:
        file_name (str): name of the file e.g. 'file.txt'
        master (bool, optional): _description_. Defaults to False.

    Returns:
        pd.DataFrame: DataFrame

    """
    if master == True and file_name[-3:]=='txt':
        master_data = pd.read_csv(
            filepath_or_buffer=f'{__dir__}/data/{str(file_name)}', delimiter='\t', encoding='shift-jis', dtype='object')
        return master_data
    elif master == True:
        master_data = pd.read_csv(
            filepath_or_buffer=f'{__dir__}/data/{str(file_name)}', encoding='shift-jis', dtype='object')
        return master_data
    else:
        column_master_data = pd.read_csv(
            filepath_or_buffer=f'{__dir__}/data/{str("mst_column_name.txt")}', delimiter='\t', encoding='shift-jis', dtype='object')
        columns = column_master_data.column_name_en
        data = pd.read_csv(
            filepath_or_buffer=f'{__dir__}/data/{str(file_name)}', encoding='shift-jis', header=None, dtype='object')
        data.columns = columns
        return data

def get_diff_data(file_name, diff_file=True):
    """_summary_

    Args:
        file_name (str): regular expression that specifies a file pattern e.g. 'file_*.txt'
        diff_file (bool, optional): Optional boolean. Defaults to True.

    Returns:
        pd.DataFrmae: Concatenated DataFrame with proper column names
    """
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

    # Read header data
    mst = get_data(file_name='mst_column_name.txt', master=True)
    print('Return Master data')
    display(mst.head(3))
    display(mst.info(verbose=True))

    # Read all shizuoka data
    data = get_data(file_name='22_shizuoka_all_20210331.csv', master=False)
    print('Return Data after Renaming Column')
    display(data.head(3))
    display(data.info(verbose=True))

    # Read all diff data
    diff_data = get_diff_data(file_name="diff*.csv", diff_file=True)
    print('Iteration Data Test')
    display(diff_data.head(3))
    display(diff_data.info(verbose=True))
