from flask import Flask
from flask import request
from flask import jsonify
import joblib
import json
import sys
import pandas as pd

from preprocessing import cleaning_data
from predict import prediction

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_method():
    return "It's alive!"

@app.route('/predict', methods=['GET', 'POST'])
def predict_method():
    #handle the POST request
    if request.method == 'POST':
        data = request.form
        #return data
        preprocess_output = cleaning_data.preprocess(data)
        if type(preprocess_output) is dict:
            return preprocess_output
        output_data = prediction.predict(preprocess_output)
        return output_data
    #otherwise handle the GET request
    return '''Please submit data of apartment / house. See the following format: 
                {
                "data": {
                    "area": int,
                    "property-type": "APARTMENT" | "HOUSE",
                    "rooms-number": int,
                    "zip-code": int,
                    "land-area": Optional[int],
                    "garden": Optional[bool],
                    "garden-area": Optional[int],
                    "equipped-kitchen": Optional[bool],
                    "full-address": Optional[str],
                    "swimming-pool": Optional[bool],
                    "furnished": Optional[bool],
                    "open-fire": Optional[bool],
                    "terrace": Optional[bool],
                    "terrace-area": Optional[int],
                    "facades-number": Optional[int],
                    "building-state": Optional[
                        "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
                    ]
                }
            }'''

if __name__ == '__main__':
    app.run(debug=True, port=105)