"""
Central configuration module of webstr selenium tests.

This module provides configuration options along with default values and
function to redefine values.
"""

# Copyright 2016 Red Hat
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
import sys


SELENIUM_LOG_LEVEL = logging.INFO
SCHEME = 'https'
PORT = 443
BROWSER = 'Firefox'
BROWSER_VERSION = ''
BROWSER_PLATFORM = 'ANY'
SELENIUM_SERVER = 'selenium-grid.example.com'
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
