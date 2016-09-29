import json

import requests

from server.settings import MARANTZ_URL


###
# Control functions
###
def power(value):
    """
    Turns the device on or off. Expects 'on' or 'off'.
    """
    if not isinstance(value, basestring):
        raise ValueError('Value must be a string.')

    cmd = "PutZone_OnOff/%s" % value.upper()
    return _send_command(cmd)


def source(value):
    """
    Changes the input source on the device.
    """
    if not isinstance(value, basestring):
        raise ValueError('Value must be a string.')

    cmd = "PutZone_InputFunction/%s" % value.upper()
    return _send_command(cmd)


def volume(value):
    """
    Changes the volume on the device.
    """
    if not isinstance(value, float):
        raise ValueError('Value must be a float.')

    value -= 80.0
    cmd = "PutMasterVolumeSet/%s" % value
    return _send_command(cmd)


def halo():
    """
    Play halo.
    """
    data = {
        'cmd0': "PutZone_OnOff/ON",
        'cmd1': "PutZone_InputFunction/GAME",
    }
    _send_command(data=data)
    return volume(39.0)


def music():
    """
    Play music.
    """
    data = {
        'cmd0': "PutZone_OnOff/ON",
        'cmd1': "PutZone_InputFunction/CD",
    }
    _send_command(data=data)
    return volume(50.0)


###
# API utilities
###
def _get_cookies():
    return {'ZoneName': 'MAIN%20ZONE	'}


def _get_headers():
    return {'referer': MARANTZ_URL % '/MainZone/index.html'}


def _send_command(cmd0=None, data=None):
    """
    Send a command to the Marantz device.
    """
    if cmd0:
        data = {
            'cmd0': cmd0
        }
    elif not data:
        raise ValueError('send_command received only None arguments.')

    response = requests.post(MARANTZ_URL % '/MainZone/index.put.asp', data=data,
                             cookies=_get_cookies(), headers=_get_headers())
    return json.dumps({'status': response.status_code})
