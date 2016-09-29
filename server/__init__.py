import os
import sys

# Determining the project root. # TODO figure out a cleaner way to do this
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)) + '/../'
sys.path.append(PROJECT_ROOT)

from flask import Flask
from flask_restful import output_json

from server.receiver import api

###
# App setup
###
app = Flask(__name__)

# Setup device routes (must come after app declaration)
from server import multi_device_routes
from server.receiver import routes


###
# Error handlers
###
@app.errorhandler(400)
def handle_http_exception(error):
    error.data['status'] = 400
    return output_json(error.data, 400)


if __name__ == '__main__':
    app.run(debug=True)
