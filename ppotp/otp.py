# -*- coding: utf-8 -*-
"""Tool to generate One-Time Passwords

Author: Peter Pakos <peter.pakos@wandisco.com>

Copyright (C) 2018 WANdisco

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

from __future__ import print_function
from .__version__ import __version__
import argparse
import os
import pyotp
import binascii
from pplogger import get_logger

__app_name__ = os.path.splitext(__name__)[0].lower()

parser = argparse.ArgumentParser(description='Tool to generate One-Time Passwords', add_help=False)
parser.add_argument('--version', action='version', version='%s %s' % (__app_name__, __version__))
parser.add_argument('--help', action='help', help='show this help message and exit')
parser.add_argument('--debug', action='store_true', dest='debug', help='debugging mode')
parser.add_argument('key', help='key or service name from ~/.otpkeys')
args = parser.parse_args()

log = get_logger(name=__name__, debug=args.debug)


def totp(key):
    try:
        code = pyotp.TOTP(key).now()
        return code
    except (TypeError, binascii.Error):
        return False


def main():
    log.debug(args)

    keys = {}
    key_file = os.path.join(os.path.expanduser('~'), '.otpkeys')

    if os.path.isfile(key_file):
        log.debug('Parsing key file %s' % key_file)
        with open(key_file, 'r') as f:
            for line in f:
                if line != '\n':
                    service = line.partition('=')[0].strip()
                    key = line.partition('=')[2].strip().replace(' ', '')
                    if service and key:
                        keys[service] = key
                        log.debug('Loaded %s' % service)

    if args.key in keys:
        log.debug('Service matched: %s' % args.key)
        key = keys[args.key]
    else:
        log.debug('No service matched, using provided key')
        key = args.key

    code = totp(key)

    if code:
        log.info(code)
    else:
        log.error('KEY ERROR')
        exit(1)
