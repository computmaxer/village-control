import json

from flask_restful.reqparse import RequestParser

import requests


MARANTZ = 'http://172.16.2.4%s'


def get_cookies():
    return {'ZoneName': 'MAIN%20ZONE	'}


def get_headers():
    return {'referer': MARANTZ % '/MainZone/index.html'}


def send_command(cmd0=None, data=None):
    """
    Send a command to the Marantz device.
    """
    if cmd0:
        data = {
            'cmd0': cmd0
        }
    elif not data:
        raise ValueError('send_command received only None arguments.')

    response = requests.post(MARANTZ % '/MainZone/index.put.asp', data=data,
                             cookies=get_cookies(), headers=get_headers())
    return json.dumps({'status': response.status_code})


class ApiReqParser(RequestParser):
    """
    Subclass of RequestParser to set some defaults, DRY up usages.
    """

    def __init__(self, **kwargs):
        # Enable trim
        super(ApiReqParser, self).__init__(
            bundle_errors=True, trim=True, **kwargs)

    def add_argument(self, *args, **kwargs):
        # Default some arguments
        if 'case_sensitive' not in kwargs:
            kwargs['case_sensitive'] = False
        if 'nullable' not in kwargs:
            kwargs['nullable'] = False
        if 'required' not in kwargs:
            kwargs['required'] = True
        return super(ApiReqParser, self).add_argument(*args, **kwargs)

    def parse_args(self, req=None, strict=True):
        return super(ApiReqParser, self).parse_args(req, strict)
