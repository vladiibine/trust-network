#!/usr/bin/env python

import os
os.environ.setdefault('TORNADO_MODULE_SETTINGS', 'settings.development')

import readline
from pprint import pprint

from trust_network_backend.app import *
from trust_network_backend.server import *


def make_shell():
    os.environ['PYTHONINSPECT'] = 'True'


def main():
    print('Loading shell...')
    make_shell()

if __name__ == '__main__':
    main()
