import pandas as pd
import numpy as np
import os
from IPython.core.display import display

# Change directory
os.chdir('../')
# Enable dynamic loading to a file.

__dir__ = os.getcwd()

# Define get_data funciton to pull data
def get_data(file_name, columns=None, master=False):
    if master == True:
        master_data = pd.read_csv(filepath_or_buffer=f'{__dir__}/data/{str(file_name)}', delimiter='\t', encoding='shift-jis')
        return master_data
    else:
        column_master_data = pd.read_csv(filepath_or_buffer=f'{__dir__}/data/{str("mst_column_name.txt")}', delimiter='\t', encoding='shift-jis')
        columns = column_master_data.column_name_en
        data = pd.read_csv(filepath_or_buffer=f'{__dir__}/data/{str(file_name)}', encoding='shift-jis', header=None)
        data.columns = columns
        return data


# Testing my code
if __name__ == '__main__':
    #pd.read_csv(__dir__+'/data/mst_column_name.txt', delimiter='\t', encoding='shift-jis')
    #pd.read_csv(filepath_or_buffer=f'{__dir__}/data/mst_column_name.txt', delimiter='\t', encoding='shift-jis')
    #pd.read_csv(filepath_or_buffer=f'{__dir__}/data/{str("mst_column_name.txt")}', delimiter='\t', encoding='shift-jis')

    # Read header data
    mst = get_data(file_name='mst_column_name.txt', master=True)
    # Read all shizuoka data
    data = get_data(file_name='22_shizuoka_all_20210331.csv', master=False)
    display(mst.head(3))
    display(data.head(3))