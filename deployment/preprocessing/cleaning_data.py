"""Import libraries"""
import pandas as pd
import numpy as np
from pandas.api.types import is_string_dtype

"""Initialize data"""
output_data = {}

"""Function to load input dictionary into a dataframe"""
def load_input(input_data):
    df_input = pd.DataFrame.from_dict(input_data, orient='index')
    return df_input

"""Function to check if required information is not empty"""
def check_required_missing(df_input):
    switch = 0
    while switch == 0:
        if df_input["area"].isnull().values.any():   #check if 'area' is empty
            output_data["error"] = "missing required information for 'area'"
            output_data["status code"] = 400
            return output_data
        if df_input["property-type"].isnull().values.any():   #check if 'property-type' is empty
            output_data["error"] = "missing required information for 'property-type'"
            output_data["status code"] = 400
            return output_data
        if df_input["rooms-number"].isnull().values.any():   #check if 'rooms-number' is empty
            output_data["error"] = "missing required information for 'rooms-number'"
            output_data["status code"] = 400
            return output_data
        if df_input["zip-code"].isnull().values.any():   #check if 'zip-code' is empty
            output_data["error"] = "missing required information for 'zip-code'"
            output_data["status code"] = 400
            return output_data
        switch =+ 1
    return output_data

"""Function to check if required information is in correct format"""
def check_required_string(df_input):
    switch = 0
    while switch == 0:
        if is_string_dtype(df_input.loc["data", "area"]):   #check if 'area' is an integer
            output_data["error"] = "'area' information must be an integer"
            output_data["status code"] = 400
            return output_data
        if is_string_dtype(df_input.loc["data", "rooms-number"]):   #check if 'rooms-number' is an integer
            output_data["error"] = "'rooms-number' information must be an integer"
            output_data["status code"] = 400
            return output_data
        if is_string_dtype(df_input.loc["data", "zip-code"]):   #check if 'zip-code' is an integer
            output_data["error"] = "'zip-code' information must be an integer"
            output_data["status code"] = 400
            return output_data
        switch =+ 1
    return output_data

"""Function to check if 'property-type' is in correct format"""
def check_property_type(df_input):
    if df_input.loc["data", "property-type"] == "APARTMENT" or df_input.loc["data", "property-type"] == "HOUSE":   #check if 'property-type' is 'APARTMENT'
        return output_data                                                                                         # or 'HOUSE'
    else:
        output_data["error"] = "'property-type' information can only be 'APARTMENT' or 'HOUSE'"
        output_data["status code"] = 400
        return output_data

"""Function to rename input features to match model training features and drop features that won't be used for modeling, if all required information are available 
    and in correct format"""
def input_features(df_input):
    df_input.rename(columns = {"area":"livingArea", "property-type":"type", "rooms-number":"bedrooms", "zip-code":"postalCode", "equipped-kitchen":"kitchenType", 
    "facades-number":"numberOfFrontages", "building-state":"buildingCondition"}, inplace=True)   #rename features to match train-test set
    df_input.drop(df_input.columns[8:14], inplace=True, axis=1)   #drop features that won't be used for prediction
    df_input.drop(df_input.columns[4:7], inplace=True, axis=1)   #drop features that won't be used for prediction
    df_input = df_input.reindex(sorted(df_input.columns), axis=1)   #sort features alphabetically
    return df_input

"""Function to transform input values"""
def input_values(df_input_features):
    if df_input_features.loc["data", "type"] == "APARTMENT":   #transform 'property-type' to binary
        df_input_features.loc["data", "type"] = 0
    elif df_input_features.loc["data", "type"] == "HOUSE":
        df_input_features.loc["data", "type"] = 1
    df_input_features["type"] = df_input_features["type"].astype(int)   #convert 'property-type' to integer
    df_input_features["postalCode"] = df_input_features["postalCode"].astype(str)   #convert 'zip-code' to string type
    if df_input_features.loc["data", "kitchenType"] == False:   #convert 'equipped-kitchen' to binary
        df_input_features.loc["data", "kitchenType"] = 0
    elif df_input_features.loc["data", "kitchenType"] == True:
        df_input_features.loc["data", "kitchenType"] = 1
    else:
        df_input_features.loc["data", "kitchenType"] = 0   #default to 0 if empty
    df_input_features["kitchenType"] = df_input_features["kitchenType"].astype(int)   #convert 'equipped-kitchen' to integer
    if df_input_features.loc["data", "buildingCondition"] == "NEW":   #transform 'building-state' to numeric
        df_input_features.loc["data", "buildingCondition"] = 1
    elif df_input_features.loc["data", "buildingCondition"] == "JUST RENOVATED":
        df_input_features.loc["data", "buildingCondition"] = 2
    elif df_input_features.loc["data", "buildingCondition"] == "GOOD":
        df_input_features.loc["data", "buildingCondition"] = 3
    elif df_input_features.loc["data", "buildingCondition"] ==  "TO RENOVATE":
        df_input_features.loc["data", "buildingCondition"] = 5
    elif df_input_features.loc["data", "buildingCondition"] ==  "TO REBUILD":
        df_input_features.loc["data", "buildingCondition"] = 6
    else:
        df_input_features.loc["data", "buildingCondition"] = 0   #default to 0 if empty
    df_input_features["buildingCondition"] = df_input_features["buildingCondition"].astype(int)   #convert 'building-state' to integer
    if df_input_features["numberOfFrontages"].isnull().values.any():   #check if 'facades-number' is empty
        df_input_features.loc["data", "numberOfFrontages"] = 1   #default to 1 if empty
    if is_string_dtype(df_input_features.loc["data", "numberOfFrontages"]):   #check 'facades-number' value
        df_input_features.loc["data", "numberOfFrontages"] = 1   #default to 1 if string type
    df_input_features["numberOfFrontages"] = df_input_features["numberOfFrontages"].astype(int)   #convert 'facades-number' to integer
    return df_input_features

"""This is the main preprocessing function"""
def preprocess(input_data):
    df_input = load_input(input_data)
    output_missing = check_required_missing(df_input)
    if len(output_missing) != 0:
        return output_missing
    output_string = check_required_string(df_input)
    if len(output_string) != 0:
        return output_string
    output_type = check_property_type(df_input)
    if len(output_type) != 0:
        return output_type
    df_input_features = input_features(df_input)
    df_input_values = input_values(df_input_features)
    return df_input_values