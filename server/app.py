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

def main():
    os.system('py -m scraper.py')

if __name__ == '__main__':
    main()
    app.run()
    