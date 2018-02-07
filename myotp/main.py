#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tool to generate One-Time Passwords

Author: Peter Pakos <peter.pakos@wandisco.com>

Copyright (C) 2017 WANdisco

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import, print_function

import argparse
import os
import sys
import pyotp
import binascii

from . import VERSION


class Main(object):
    _version = VERSION
    _name = os.path.basename(sys.argv[0])

    def __init__(self):
        self._key_file = os.path.join(os.path.expanduser('~'), '.otpkeys')
        self._parse_args()
        self._keys = {}

        if os.path.isfile(self._key_file):
            with open(self._key_file, 'r') as f:
                for line in f:
                    if line != '\n':
                        service = line.partition('=')[0].strip()
                        key = line.partition('=')[2].strip().replace(' ', '')
                        if service and key:
                            self._keys[service] = key

    def _parse_args(self):
        parser = argparse.ArgumentParser(description='Tool to generate One-Time Passwords', add_help=False)
        parser.add_argument('--help', action='help', help='show this help message and exit')
        parser.add_argument('--version', action='version', version='%s %s' % (self._name, self._version))
        parser.add_argument('key', help='key or service name from ~/.otpkeys')
        self._args = parser.parse_args()

    @staticmethod
    def _totp(key):
        try:
            code = pyotp.TOTP(key).now()
            return code
        except (TypeError, binascii.Error):
            return False

    def run(self):
        if self._args.key in self._keys:
            key = self._keys[self._args.key]
        else:
            key = self._args.key

        code = self._totp(key)

        if code:
            print(code)
        else:
            print('KEY ERROR', file=sys.stderr)
            exit(1)


def main():
    try:
        Main().run()
    except KeyboardInterrupt:
        print('\nCancelling...')
        exit(130)
