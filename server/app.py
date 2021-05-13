from flask import Flask, jsonify
from flask_cors import CORS
import os


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/', methods=['GET'])
def home():
    # path of the folder containing the raw images
    inPath ="data/images/"

    for imagePath in os.listdir(inPath):
            # imagePath contains name of the image 
            # set all the information from the data in images and csv
            os.system('py anpr.py --i data/images/'+imagePath)

    return "Works"


if __name__ == '__main__':
    app.run()
    