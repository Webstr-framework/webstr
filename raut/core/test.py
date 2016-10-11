# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Core test case class(es) and exceptions.

Author: pnovotny, ltrilety
"""

import logging

from selenium.common import exceptions as selenium_ex

import raut.lib.selenium.ui.exceptions as ui_exceptions
from raut.lib.driver import Driver
from raut.core import config

LOGGER = logging.getLogger(__name__)

SELENIUM_LOGGER = logging.getLogger('selenium.webdriver.remote.remote_connection')
SELENIUM_LOGGER.setLevel(config.SELENIUM_LOG_LEVEL)


class UITestCase(object):
    """
    Base class for all Selenium-based test cases.
    By default starts new browser at set_up() and quits it at tear_down().
    """
    TEST_FAILURE_EXCEPTIONS = (ui_exceptions.GeneralException,
                               selenium_ex.WebDriverException,
                               AssertionError)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.driver = None

    def _start_browser(self):
        """ Open new browser or get driver instance of the existing one. """
        self.driver = Driver.get_default_driver()
        self.driver.maximize_window()

    def _quit_browser(self):
        """ Quit browser and remove its cached driver instance. """
        self.driver.quit()
        self.driver = None
        Driver.destroy_default_driver()

    def set_up(self):
        """ Open new browser (if not already opened). """
        self._start_browser()

    def tear_down(self):
        """ Close browser. """
        self._quit_browser()

    def fail(self, *args):
        """Raise `TestFailedError` as indication of test failure.

        :param *args: optional arguments to pass to the exception instance
        """
        raise TestFailedError(str(*args))


class TestFailedError(ui_exceptions.GeneralException):
    """ Test Error """
    message = "Test failed"


class TestSetUpFailed(ui_exceptions.GeneralException):
    """ Test set up fail """
    message = "!!! TEST SETUP FAILED !!!"


class TestTearDownFailed(ui_exceptions.GeneralException):
    """ Test tear down fail """
    message = "!!! TEST TEAR DOWN FAILED !!!"


class TestExecutionFailed(ui_exceptions.GeneralException):
    """ Test fail """
    message = "!!! TEST EXECUTION FAILED !!!"
