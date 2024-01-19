"""
Device class for inheriting to make 'drivers' for specific devices
"""


class Device:
    def __init__(self, devicename):
        self.devicename = devicename
        self.dev = None
