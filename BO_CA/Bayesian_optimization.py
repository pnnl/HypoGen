import pandas as pd
import numpy as np
from scipy import spatial

import sklearn.gaussian_process as gp
from sklearn.model_selection import train_test_split
#from bayes_opt import BayesianOptimization
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LassoCV
from xgboost import XGBRegressor
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt



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
















all_data_parameter = pd.concat([initial_data_parameter, data_BO_parameter], axis = 0, ignore_index=True)


all_data_parameter_X = all_data_parameter.drop('y', axis=1)
X_train, X_test, y_train, y_test = train_test_split(all_data_parameter_X, all_data_parameter['y'], 
                                                    test_size=0.2, random_state=123)








rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
importances_rf = pd.Series(rf.feature_importances_, index=data_BO_parameter_X.columns)
sorted_importances_rf = importances_rf.sort_values()
sorted_importances_rf


# Feature importance from LassoCV
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lasso = LassoCV(cv=5, random_state=42, max_iter=10000)
lasso.fit(X_train_scaled, y_train)

importances_lasso = pd.Series(np.abs(lasso.coef_), index=data_BO_parameter_X.columns)
sorted_importances_lasso = importances_lasso.sort_values()
sorted_importances_lasso


# Create XGBoost model
xgb = XGBRegressor(n_estimators=100, random_state=42)

# Fit the model
xgb.fit(X_train, y_train)
# Get feature importances
importances_xgb = pd.Series(xgb.feature_importances_, index=data_BO_parameter_X.columns)
sorted_importances_xgb = importances_xgb.sort_values()
sorted_importances_xgb


fig, ax = plt.subplots(3, 1, figsize=(10, 15))  # Adjust as needed

sorted_importances_rf.plot(kind='barh', ax=ax[0], color='lightgreen')
ax[0].set_title('Feature Importance from Random Forest')
ax[0].tick_params(axis='both', which='major', labelsize=12)  # Adjust as needed

sorted_importances_lasso.plot(kind='barh', ax=ax[1], color='lightblue')
ax[1].set_title('Feature Importance from LassoCV')
ax[1].tick_params(axis='both', which='major', labelsize=12)  # Adjust as needed

sorted_importances_xgb.plot(kind='barh', ax=ax[2], color='skyblue')
ax[2].set_title('Feature Importance from XGBoost')
ax[2].tick_params(axis='both', which='major', labelsize=12)  # Adjust as needed

plt.tight_layout()
plt.show()




all_data_parameter_X_FI = all_data_parameter_X[['temp', 'flu', 'melting', 'Labutes', 'octanol', 'molar', 'polar']]

X_train, X_test, y_train, y_test = train_test_split(all_data_parameter_X_FI, all_data_parameter['y'], 
                                                    test_size=0.2, random_state=123)

cmean=[1.0]*7
cbound=[[1e-3, 1e3]]*7

kernel = C(1.0, (1e-3,1e3)) * gp.kernels.RBF(cmean,cbound)

model = gp.GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=100, normalize_y=True)

model.fit(X_train, y_train)
params = model.kernel_.get_params()

y_pred, std = model.predict(X_test, return_std=True)

pbounds = {
       'octanol': (-1, 0), 'molar': (0, 10), 
       'polar': (0, 25), 'Labutes': (0, 15),
       'melting': (0, 45)}
fluorenone_ls = list(np.linspace(40.0, 70.0, 7))





bo_result_ls = []

for flu in fluorenone_ls:
    def black_box_function(melting, Labutes, octanol, molar, polar):
        temperature_1 = 25
        temperature_2 = 50
        fluorenone = flu

        temp_row_1 = np.array([temperature_1, fluorenone, melting, Labutes, octanol, molar, polar])


        temp_row_2 = np.array([temperature_2, fluorenone, melting, Labutes, octanol, molar, polar])

        RT_pred = model.predict(temp_row_1.reshape(1, -1), return_std=False).item()
        HT_pred = model.predict(temp_row_2.reshape(1, -1), return_std=False).item()

        return RT_pred - HT_pred

    optimizer = BayesianOptimization(
        f=black_box_function,
        pbounds=pbounds,
        random_state=321,
        verbose=1
    )
    
    optimizer.maximize(
    init_points=100,
    n_iter=500,
    acq='ei',
    kappa=2.576,
    kappa_decay=1,
    kappa_decay_delay=0,
    xi=0.0
    )

    bo_result_ls.append(optimizer.max)



target_gpr = []
for i in range(len(bo_result_ls)):
    target_gpr.append(bo_result_ls[i]['target'])


plt.figure()
plt.plot(fluorenone_ls[:7], target_gpr, color='green', marker='o', linestyle='dashed',
     linewidth=2, markersize=12)
plt.xlabel('Fluorenone')
plt.ylabel('Target')
plt.show()







parameter_temp = parameter.drop('carboxylic acid number', axis=1)
parameter_temp.columns = ['name', 'MW', 'hydroxyl', 'amino', 'carbon', 'octanol', 'molar', 'polar', 
                          'Labutes', 'Balabans', 'Bertz', 'melting']

# parameter_temp_FI = parameter_temp.loc[:, ['name', 'MW', 'melting', 'Labutes', 'carbon', 'Bertz', 'octanol']]
parameter_temp_FI = parameter_temp.loc[:, ['name', 'MW', 'melting', 'Labutes', 'octanol', 'molar', 'polar']]


# optimal_parameter = np.array([19.81943418737145, 8.622163938480561, 0.3893212505920849, 19.405973068587766, -0.49206881138825054])
optimal_parameter = np.array([28.9910590366565, 8.605522931730595, -0.5303020156228744, 1.1441647817115663, 18.087022162887525])


from scipy.optimize import minimize

# Define new objective function
def objective(p, x_c):
    return np.mean(np.abs((p * x_c - optimal_parameter) / optimal_parameter))

results = []

for i in range(parameter_temp_FI.shape[0]):
    x_c = parameter_temp_FI.iloc[i,2:].values
    
    constraints = [{'type': 'ineq', 'fun': lambda p: 0.2 - p},
                   {'type': 'ineq', 'fun': lambda p: p}]

    # Initial guess
    p0 = 0.03

    # Perform optimization for each candidate
    result = minimize(objective, p0, args=(x_c), constraints=constraints)
    
    # Save result along with row index
    results.append((result.fun, i, result.x))

# Sort results by objective value (the lower the better)
results.sort(key=lambda x: x[0])

# Print top three combinations
for r in results[:10]:
    print(f"Row: {r[1]}, Percent: {r[2]}, Objective: {r[0]}")



from scipy.optimize import minimize

# Define new objective function
def objective(p, x_c1, x_c2):
    return np.mean(np.abs((p[0] * x_c1 + p[1] * x_c2 - optimal_parameter) / optimal_parameter))

results = []

# Make two loops if you want all possible pairs of rows in parameter_temp_FI
for i in range(parameter_temp_FI.shape[0]):
    for j in range(i+1, parameter_temp_FI.shape[0]):
        x_c1 = parameter_temp_FI.iloc[i,2:].values
        x_c2 = parameter_temp_FI.iloc[j,2:].values
    
        constraints = [{'type': 'ineq', 'fun': lambda p: 0.2 - p[0]},
                       {'type': 'ineq', 'fun': lambda p: p[0]},
                       {'type': 'ineq', 'fun': lambda p: 0.2 - p[1]},
                       {'type': 'ineq', 'fun': lambda p: p[1]}]

        # Initial guesses
        p0 = [0.03, 0.03]

        # Perform optimization for each candidate pair
        result = minimize(objective, p0, args=(x_c1, x_c2), constraints=constraints)
        
        # Save result along with row indices
        results.append((result.fun, i, j, result.x))

# Sort results by objective value (the lower the better)
results.sort(key=lambda x: x[0])

# Print top three combinations
for r in results[:10]:
    print(f"Rows: {r[1]}, {r[2]}, Percents: {r[3]}, Objective: {r[0]}")




                          