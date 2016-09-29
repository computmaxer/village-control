from flask import Blueprint

from flask_restful import abort

from server.receiver import api
from server.rest_helpers import ApiReqParser


receiver_module = Blueprint('receiver', __name__)


# Power
power_reqs = ApiReqParser()
power_reqs.add_argument('value', choices=('on', 'off'))


@receiver_module.route('/v1/power', methods=('PUT',))
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


@receiver_module.route('/v1/source', methods=('PUT',))
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


@receiver_module.route('/v1/volume', methods=('PUT',))
def volume():
    args = volume_reqs.parse_args()
    value = args.get('value')

    if value < 0.0 or value > 80.0:
        abort(400, message='value must be between 0 and 80')

    return api.volume(value)
