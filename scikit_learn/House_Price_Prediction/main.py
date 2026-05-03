'''
==============================================================================================================================
                        House Price Prediction Using Machine Learning Algorithms
==============================================================================================================================
'''

#importing libraries
import numpy as np
import pandas as pd

#Loading dataset
dataset = pd.read_csv("C:/Users/Admin/Documents/pyCodes/scikit_learn/House_Price_Prediction/kc_house_data.csv")
print(dataset.head())

#Selecting features (X) and target (y)
X = dataset[["bedrooms","bathrooms","sqft_living","sqft_lot","floors","condition","grade","sqft_basement","yr_built","yr_renovated"]]
y = dataset["price"].values

#Displaying shape of the dataset
print('-'*80)
print(f"Shape of X is {X.shape} \n Shape of y is {y.shape}")

#Splitting dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

print('-'*80)
print(f"Length of X_train is: {len(X_train)} \nLength of X_test is: {len(X_test)}")
print(f"Length of y_train is: {len(y_train)} \nLength of y_test is: {len(y_test)}")

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

#Fitting on training data and transform
X_train = sc.fit_transform(X_train)

#Transform test data
X_test = sc.transform(X_test)

# Convert back to DataFrame for making code look clean and neat
#This is mainly used for XGBoost and AdaBoost 
X_train = pd.DataFrame(X_train, columns=[
    "bedrooms","bathrooms","sqft_living","sqft_lot",
    "floors","condition","grade","sqft_basement",
    "yr_built","yr_renovated"
])

X_test = pd.DataFrame(X_test, columns=[
    "bedrooms","bathrooms","sqft_living","sqft_lot",
    "floors","condition","grade","sqft_basement",
    "yr_built","yr_renovated"
])

#=================================================================================================================================
#1. Implementing Linear Regression Algorithm
#=================================================================================================================================

from sklearn.linear_model import LinearRegression
model = LinearRegression()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
print('-'*80)
print("Linear Regression Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


#=================================================================================================================================
#12. Implementing Ridge Regression Algorithm
#=================================================================================================================================

from sklearn.linear_model import Ridge
model = Ridge()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("Ridge Regression Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


#=================================================================================================================================
#3. Implementing Decision Tree Regressor
#=================================================================================================================================


from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("Decision Tree Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


#=================================================================================================================================
#4. Implementing Random Forest Regressor
#=================================================================================================================================

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("Random Forest Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


#=================================================================================================================================
#5. Implementing Support Vector Regressor
#=================================================================================================================================

from sklearn.svm import SVR
model = SVR()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("SVR Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


#=================================================================================================================================
#6. Implementing KNN Regressor
#=================================================================================================================================

from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("KNN Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

#=================================================================================================================================
#7. Implementing Gradient Boost Regressor
#=================================================================================================================================

from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("Gradient Boosting Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


#=================================================================================================================================
#8. Implementing ElasticNet Regression
#=================================================================================================================================

from sklearn.linear_model import ElasticNet
model = ElasticNet()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("ElasticNet Performance:")
print("MAE:",mean_absolute_error(y_test, y_pred))


#=================================================================================================================================
#9. Implementing AdaBoost Regressor
#=================================================================================================================================

from sklearn.ensemble import AdaBoostRegressor
model = AdaBoostRegressor()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("AdaBoostRegressor Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))


#=================================================================================================================================
#10. Implementing Extra Trees Regressor
#=================================================================================================================================

from sklearn.ensemble import ExtraTreesRegressor
model = ExtraTreesRegressor()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("ExtraTreeRegressor Performance:")
print("MAE:",mean_absolute_error(y_test, y_pred))


#=================================================================================================================================
#11. Implementing LightGBM Regressor
#=================================================================================================================================

from lightgbm import LGBMRegressor
model = LGBMRegressor()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("LGBMRegressor Performance:")
print("MAE:",mean_absolute_error(y_test, y_pred))

#=================================================================================================================================
#12. Implementing XGBoost Regressor
#=================================================================================================================================

from xgboost import XGBRegressor
model = XGBRegressor()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("XGBoost Performance:")
print("MAE:",mean_absolute_error(y_test, y_pred))

'''
#=================================================================================================================================
                                                                    THE END
#=================================================================================================================================
'''

