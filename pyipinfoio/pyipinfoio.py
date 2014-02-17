#!/usr/bin/env python

"""
    Simple wrapper around the ipinfo.io IP geolocation API.
"""

import json
import subprocess as sp

class IPLookupError(Exception):
    pass

class IPLookup(object):
    def __init__(self):
        pass

    def lookup(self, ip_address, param=None):
        """
            Returns a dictionary info regarding the given IP address.
            If a specific parameter is supplied (city, country), a string is
            returned.
        """

        cmd = 'curl -s ipinfo.io/'
        if param:
            cmd += '{}/{}'.format(ip_address, param)
        else:
            cmd += ip_address
        cmd_obj = sp.Popen(cmd, stdout=sp.PIPE, shell=True)
        cmd_out = cmd_obj.communicate()[0].strip()

        if cmd_out == 'null':
            cmd_out = None

        # error handling
        if cmd_out == 'Please provide a valid IP address':
            raise IPLookupError("Invalid IP address")
        elif cmd_out == 'undefined':
            raise IPLookupError("Invalid parameter")

        if param:
            return cmd_out
        else:
            return json.loads(cmd_out)
