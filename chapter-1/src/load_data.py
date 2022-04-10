import pandas as pd
import numpy as np
import os

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
        #data = pd.read_csv(filepath_or_buffer=__dir__+'\\data\\'+file_name, delimiter='\t', encoding='shift-jis', header=None)
        data.columns = columns
        return data


# Testing my code

pd.read_csv(__dir__+'/data/mst_column_name.txt', delimiter='\t', encoding='shift-jis')
pd.read_csv(filepath_or_buffer=f'{__dir__}/data/mst_column_name.txt', delimiter='\t', encoding='shift-jis')
pd.read_csv(filepath_or_buffer=f'{__dir__}/data/{str("mst_column_name.txt")}', delimiter='\t', encoding='shift-jis')
# Read header data
mst = pd.read_csv('./data/mst_column_name.txt', delimiter='\t', encoding='shift-jis')
mst.head(3)

# Read all shizuoka data
data = pd.read_csv('./data/22_shizuoka_all_20210331.csv', header=None, columns=mst.column_name_en.values)
