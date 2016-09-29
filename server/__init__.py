import os
import sys

# Determining the project root. # TODO figure out a cleaner way to do this
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)) + '/../'
sys.path.append(PROJECT_ROOT)

from flask import Flask
from flask_restful import output_json

from server.receiver import receiver_module
from server.recipes import recipes_module
from server.settings import BASE_API

###
# App setup
###
app = Flask(__name__)

app.register_blueprint(receiver_module, url_prefix=BASE_API % '/receiver')
app.register_blueprint(recipes_module, url_prefix=BASE_API % '/recipes')


###
# Error handlers
###
@app.errorhandler(400)
def handle_http_exception(error):
    error.data['status'] = 400
    return output_json(error.data, 400)


if __name__ == '__main__':
    app.run(debug=True)
