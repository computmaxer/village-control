from flask import Flask

from flask_restful import abort
from flask_restful import output_json

import api
from utils import ApiReqParser

app = Flask(__name__)

BASE_API = '/api%s'


###
# Built-in functionality
###

# Power
power_reqs = ApiReqParser()
power_reqs.add_argument('value', choices=('on', 'off'))


@app.route(BASE_API % '/power', methods=('PUT',))
def power():
    args = power_reqs.parse_args()
    return api.power(args.get('value'))


# Source
source_reqs = ApiReqParser()
source_reqs.add_argument(
    'value',
    choices=(
        # Built-in
        'sat/cbl', 'tv', 'bd', 'game', 'cd', 'mplay', 'nethome', 'aux1', 'aux2',
        # Custom names
        'xbox', 'chromecast', 'alexa', 'music'
    ))


@app.route(BASE_API % '/source', methods=('PUT',))
def source():
    args = source_reqs.parse_args()
    value = args.get('value')

    # Setup custom source handlers
    if value == 'xbox':
        value = 'game'
    elif value == 'chromecast':
        value = 'mplay'
    elif value == 'alexa' or value == 'music':
        value = 'cd'

    return api.source(value)


# Volume
volume_reqs = ApiReqParser()
volume_reqs.add_argument('value', type=float)


@app.route(BASE_API % '/volume', methods=('PUT',))
def volume():
    args = volume_reqs.parse_args()
    value = args.get('value')

    if value < 0.0 or value > 80.0:
        abort(400, message='value must be between 0 and 80')

    return api.volume(value)


###
# Convenience functions
###
@app.route(BASE_API % '/halo', methods=('PUT',))
def halo():
    return api.halo()


@app.route(BASE_API % '/music', methods=('PUT',))
def music():
    return api.music()


###
# Error handlers
###
@app.errorhandler(400)
def handle_http_exception(error):
    error.data['status'] = 400
    return output_json(error.data, 400)


if __name__ == '__main__':
    app.run(debug=True)
