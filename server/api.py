from utils import send_command


def power(value):
    """
    Turns the device on or off. Expects 'on' or 'off'.
    """
    if not isinstance(value, basestring):
        raise ValueError('Value must be a string.')

    cmd = "PutZone_OnOff/%s" % value.upper()
    return send_command(cmd)


def source(value):
    """
    Changes the input source on the device.
    """
    if not isinstance(value, basestring):
        raise ValueError('Value must be a string.')

    cmd = "PutZone_InputFunction/%s" % value.upper()
    return send_command(cmd)


def volume(value):
    """
    Changes the volume on the device.
    """
    if not isinstance(value, float):
        raise ValueError('Value must be a float.')

    value -= 80.0
    cmd = "PutMasterVolumeSet/%s" % value
    return send_command(cmd)


def halo():
    """
    Play halo.
    """
    data = {
        'cmd0': "PutZone_OnOff/ON",
        'cmd1': "PutZone_InputFunction/GAME",
    }
    send_command(data=data)
    return volume(39.0)


def music():
    """
    Play music.
    """
    data = {
        'cmd0': "PutZone_OnOff/ON",
        'cmd1': "PutZone_InputFunction/CD",
    }
    send_command(data=data)
    return volume(50.0)
