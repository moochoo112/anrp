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
    date = csv[csv[0] == plateNumber][1]
    date = date.to_string()
    return date

def main():
    os.system('py -m scraper.py')

if __name__ == '__main__':
    # main()
    app.run()
    