# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Central configuration module of raut selenium tests.

This module provides configuration options along with default values and
function to redefine values.
"""


import logging
import sys


SELENIUM_LOG_LEVEL = logging.INFO
SCHEME = 'https'
PORT = 443
BROWSER = 'Firefox'
BROWSER_VERSION = ''
BROWSER_PLATFORM = 'ANY'
SELENIUM_SERVER = 'selenium-grid.usersys.redhat.com'
SELENIUM_PORT = 4444
BROWSER_WIDTH = 1280
BROWSER_HEIGHT = 1024


def update_value(key_name, value, force=False):
  """
  Update single value of this config module.
  """
  this_module = sys.modules[__name__]
  key_name = key_name.upper()
  # raise AttributeError if we try to define new value (unless force is used)
  if not force:
    getattr(this_module, key_name)
  setattr(this_module, key_name, value)
