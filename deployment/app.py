from flask import Flask
from flask import request
from flask import jsonify
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
        #input_data = json.loads(data)
        #df_input_values = cleaning_data.preprocess(input_data)
        #output_data = prediction.predict(df_input_values)
        return data
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