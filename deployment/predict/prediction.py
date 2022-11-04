"""Import libraries"""
import pandas as pd
import numpy as np
from pandas.api.types import is_string_dtype
import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor

"""Inititalize data"""
output_data = {}

"""This is the prediction function"""
def predict(df_input_values):
    type_input = df_input_values['type'].values   #convert 'type' to numpy array
    ohe_column = df_input_values[["postalCode"]].astype(str) #declare 'postalCode' as categorical feature
    encoder = joblib.load('model/encoder.joblib')   #call saved OneHotEncoder
    ohe_transform = encoder.transform(ohe_column).toarray()   #transform categorical feature and convert to numpy array
    ohe_input = np.column_stack((type_input, ohe_transform))   #merge 'type' and 'postalCode' as encoded categorical features
    non_ohe_columns = ["bedrooms", "buildingCondition", "kitchenType", "livingArea", "numberOfFrontages"]   #declare non-categorical features
    non_ohe_input = df_input_values[non_ohe_columns].values   #convert non-categorical features to numpy array
    X_input = np.column_stack((ohe_input, non_ohe_input))   #merge data as X
    scaler = joblib.load('model/scaler.joblib')   #call saved scaler
    X_scaled = scaler.transform(X_input)   #transform X with scaler
    model = joblib.load('model/model.joblib')   #call saved model
    prediction = model.predict(X_scaled)   #predict using model
    output_data["prediction"] = prediction[0]   #save prediction to output dictionary
    output_data["status code"] = 200
    return output_data