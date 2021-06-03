from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pandas as pd


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['POST'])
def get_image_info():
    post_data = request.get_json()
    plateNumber = post_data.get('kenteken')
    csv=pd.read_csv('number_plates.csv',',', header=None)
    #reverse the data.
    reversedCsv = csv[::-1].reset_index()

    #create a list of data
    data = []

    date = reversedCsv[reversedCsv[0] == plateNumber][1]
    date = date.to_string()
    data.append(date)
    location=""
    try:
        location = reversedCsv[reversedCsv[0] == plateNumber][2].to_string()
    except:
        location = "No Location"
    data.append(" ".join(location.split()))
    return jsonify(data)

def main():
    os.system('py -m scraper.py')

if __name__ == '__main__':
    # main()
    app.run()
    