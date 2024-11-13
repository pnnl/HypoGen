import pandas as pd
import numpy as np
from scipy import spatial

import sklearn.gaussian_process as gp
from sklearn.model_selection import train_test_split
#from bayes_opt import BayesianOptimization
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

np.set_printoptions(suppress=True)

from copy import copy
import itertools
import matplotlib.pyplot as plt

from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
from sklearn.gaussian_process import GaussianProcessRegressor
from scipy.stats import norm
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C ,WhiteKernel as Wht,Matern as matk

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import seaborn as sns


data_LHS = pd.read_csv('data_LHS.csv')
data_LHS['glucose'] = 0



data_grid = pd.read_csv('data_grid.csv')
print(len(data_grid))
data_grid = data_grid[data_grid['fluorenone'] != 0]
print(len(data_grid))

data_grid = data_grid[data_grid['betaCD'] == 0]
data_grid = data_grid[data_grid['sucrose'] == 0]

data_grid = data_grid.drop(['betaCD', 'sucrose'], axis=1)
data_grid = data_grid.drop(['sodium hydroxide (mol equ)'], axis=1)
data_grid = data_grid.rename(columns = {'b-cyclodextrin':'betaCD'})

print(data_grid.shape)
data_grid['sum'] = data_grid[['betaCD', 'alphaCD', 'urea', 'sorbitol', 'glucose']].sum(axis=1)
data_grid = data_grid[data_grid['sum'] != 0]
data_grid = data_grid.drop(columns='sum')
print(data_grid.shape)

initial_data = pd.concat([data_grid, data_LHS], ignore_index=True)

def process_data(initial_data, parameter_file="descriptors/parameter_20230510.csv"):
    def get_MW(parameter, additive_name):
        return parameter[parameter['additive name'] == additive_name]['MW'].values[0]

    def get_weighted_col(data, column_name, MW):
        weighted_col = data[column_name] / MW
        return weighted_col.values.astype(float)

    def get_parameter(parameter, index):
        return parameter.iloc[index, 2:].values.astype(float)

    # Load parameter data
    parameter = pd.read_csv(parameter_file)
    parameter = parameter.drop(['classification', 'CAS', 'SMILES', 'chemical formula'], axis=1)

    # Ensure the initial_data has the correct column names
    data = initial_data.rename(columns={
        "betaCD": "b-CD",
        "alphaCD": "a-CD"
    })

    # List of additives to process
    additives = ["sorbitol", "b-CD", "glucose", "a-CD", "urea"]

    # Initialize an array with zeros to store results
    result_array = np.zeros((len(data), len(parameter.columns) - 2))

    for idx, additive in enumerate(additives):
        MW = get_MW(parameter, additive)
        weighted_col = get_weighted_col(data, additive, MW)
        weighted_col = np.nan_to_num(weighted_col)

        additive_parameter = get_parameter(parameter, idx)
        additive_parameter = np.nan_to_num(additive_parameter)

        result_array += np.outer(weighted_col, additive_parameter)

    return pd.DataFrame(result_array, columns=parameter.columns[2:])

result_df_old = process_data(initial_data)

initial_data_parameter = pd.concat([initial_data, result_df_old], axis = 1)
initial_data_parameter = initial_data_parameter.drop(columns=['betaCD', 'alphaCD', 'urea', 'sorbitol', 'glucose'])
# initial_data_parameter = initial_data_parameter.loc[:, (initial_data_parameter != 0).any(axis=0)]
initial_data_parameter.columns = ['temp', 'flu', 'y', 'hydroxyl', 'carboxylic', 'amino', 'carbon', 'octanol', 'molar', 'polar', 
                             'Labutes', 'Balabans', 'Bertz', 'melting']

initial_data_parameter = initial_data_parameter.apply(pd.to_numeric, errors='coerce')

initial_data_parameter_X = initial_data_parameter.drop('y', axis=1)



data_BO_1 = pd.read_csv('data_BO_1.csv', na_values=[''])
data_BO_1.fillna(0, inplace=True)
data_BO_2 = pd.read_csv('data_BO_2.csv', na_values=[''])
data_BO_2.fillna(0, inplace=True)
data_BO_data = pd.concat([data_BO_1, data_BO_2], ignore_index=True)


parameter = pd.read_csv("descriptors/parameter_20230510.csv")
parameter = parameter.drop(['classification', 'CAS', 'SMILES', 'chemical formula'], axis=1)


def process_data(data, parameter_file="descriptors/parameter_20230510.csv"):
    def get_MW(parameter, additive_name):
        return parameter[parameter['additive name'] == additive_name]['MW'].values[0]

    def get_weighted_col(data, column_name, MW):
        weighted_col = data[column_name] / MW
        return weighted_col.values.astype(float)

    def get_parameter(parameter, index):
        return parameter.iloc[index, 2:].values.astype(float)

    # Load parameter data
    parameter = pd.read_csv(parameter_file)
    parameter = parameter.drop(['classification', 'CAS', 'SMILES', 'chemical formula'], axis=1)

    # List of additives to process
    additives = ['urea', 'D-Ribose', 'D-Xylose', '2-Deoxy-D-glucose', '2-Deoxy-D-ribose',
       'D-Fucose', 'D-Glucosamine', 'N-Acetyl-D-glucosamine',
       'gluconic acid', 'D-Glucuronate', 'N-Acetylneuraminate',
       'D-Fructose', 'L-Sorbose']

    # Initialize an array with zeros to store results
    result_array = np.zeros((len(data), len(parameter.columns) - 2))

    for idx, additive in enumerate(additives):
        MW = get_MW(parameter, additive)
        weighted_col = get_weighted_col(data, additive, MW)
        weighted_col = np.nan_to_num(weighted_col)

        additive_parameter = get_parameter(parameter, idx+4)
        additive_parameter = np.nan_to_num(additive_parameter)

        result_array += np.outer(weighted_col, additive_parameter)

    return pd.DataFrame(result_array, columns=parameter.columns[2:])

result_df = process_data(data_BO_data)


data_BO_parameter = pd.concat([data_BO_data, result_df], axis = 1)
data_BO_parameter = data_BO_parameter.drop(columns=['urea', 'D-Ribose', 'D-Xylose', '2-Deoxy-D-glucose', '2-Deoxy-D-ribose',
       'D-Fucose', 'D-Glucosamine', 'N-Acetyl-D-glucosamine',
       'gluconic acid', 'D-Glucuronate', 'N-Acetylneuraminate',
       'D-Fructose', 'L-Sorbose'])
data_BO_parameter = data_BO_parameter.loc[:, (data_BO_parameter != 0).any(axis=0)]


data_BO_parameter.columns = ['temp', 'flu', 'y', 'hydroxyl', 'carboxylic','amino', 'carbon', 'octanol', 'molar', 'polar', 
                             'Labutes', 'Balabans', 'Bertz', 'melting']

data_BO_parameter = data_BO_parameter.apply(pd.to_numeric, errors='coerce')

data_BO_parameter_X = data_BO_parameter.drop('y', axis=1)






all_data_parameter = pd.concat([old_data_parameter, new_add_parameter], axis = 0, ignore_index=True)


all_data_parameter['y'] = -all_data_parameter['y']


bins = [44, 54, 64, 73]
labels = ["44-54", "54-64", "64-73"]
all_data_parameter['flu_range'] = pd.cut(all_data_parameter['flu'], bins=bins, labels=labels, right=False)

subset_data = all_data_parameter[(all_data_parameter['flu_range'] == "54-64")]
# print(subset_data)


def compute_correlation_by_group(df, group_by_column):
    exclude_cols = ['y', 'temp', 'flu', 'flu_range']
    correlations = df.groupby(group_by_column).apply(lambda group: group.drop(exclude_cols, axis=1).corrwith(group['y']))
    return correlations

group_by_column = 'temp'  # or 'flu_range'
# print(compute_correlation_by_group(subset_data, group_by_column))


df = compute_correlation_by_group(subset_data, group_by_column)







