# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Support functionality for Selenium WebDriver.

Author: pnovotny, ltrilety
"""

import logging
import time

from selenium.common import exceptions as selenium_ex
from selenium.webdriver.support.ui import WebDriverWait as BaseWebDriverWait

import raut.lib.selenium.ui.exceptions as ui_exceptions


LOGGER = logging.getLogger(__name__)

POLL_FREQUENCY = 1
SELENIUM_GRID_TIMEOUT = 60


class WebDriverUtils(object):
    """
    Container for utility methods

    Attributes:
        driver - webdriver instance
    """
    driver = None

    @staticmethod
    def wait_a_while(wait_time, driver=None):
        """
        Wait a while and regulary refresh the page
        note that it goes back to default page for current url,
        so when there are frames they will be reseted

        Parameters:
            wait_time - the time in seconds, it is telling how long to wait
            driver - webdriver instance, by default it uses class attribute
        """
        LOGGER.debug("wait_a_while(wait_time='%s')", wait_time)
        driver = driver or WebDriverUtils.driver
        if driver:
            seconds_waited = 0
            second_to_wait = SELENIUM_GRID_TIMEOUT - 20
            while (seconds_waited + second_to_wait) <= wait_time:
                time.sleep(second_to_wait)
                driver.refresh()
                seconds_waited += second_to_wait
            if seconds_waited < wait_time:
                time.sleep(wait_time - seconds_waited)
                # refresh not needed, just to be sure
                driver.refresh()
        else:
            raise ui_exceptions.GeneralException("No webdriver defined for wait")


class WebDriverWait(BaseWebDriverWait):
    """
    Overridden :class:`selenium.webdriver.support.ui.WebDriverWait` class.
    The only difference is updated `POLL_FREQUENCY` from 0.5 to 1 second.
    """

    def __init__(self, driver, timeout, poll_frequency=POLL_FREQUENCY, **kwargs):
        super(WebDriverWait, self).__init__(driver, timeout, poll_frequency, **kwargs)


class WaitForPageObject(object):
    """
    Wrapper around WebDriverWait providing helper methods for page objects.

    Usage::
        template = TemplateInstance(driver, name='test-tmpl')

        WaitForPageObject(template, 60).to_disappear()
        WaitForPageObject(template, 30).status('is_ok')
        WaitForPageObject(template, 30).status_not('is_locked')
        ...
    """
    __IGNORED_EXCEPTIONS = ui_exceptions.InitPageValidationError
    __DISAPPEAR_TIMEOUT = 1

    def __init__(self, page_object, timeout=None):
        timeout = timeout or 0
        self.__page_object = page_object
        self.__wait = WebDriverWait(
          driver=self, timeout=timeout,
          ignored_exceptions=self.__IGNORED_EXCEPTIONS)

    @property
    def __validated_page_object(self):
        """Runs init validation before the page object is returned."""
        self.__page_object._initial_page_object_validation()
        return self.__page_object

    def to_disappear(self, message=None):
        """
        Waits until the page object is no longer present on the page.

        Parameters:
            message (str): error message
        """
        message = message or '%s is still present' % self.__page_object
        original_timeout = self.__page_object._timeout
        self.__page_object.driver.implicitly_wait(self.__DISAPPEAR_TIMEOUT)
        try:
            self.__wait.until_not(lambda self: self.__validated_page_object,
                                  message=message)
        except selenium_ex.TimeoutException as ex:
            self.__page_object.driver.implicitly_wait(original_timeout)
            raise ex

    def status(self, status_prop, message=None):
        """
        Waits until page object property `status_prop` is evaluated as True.

        Parameters:
            status_prop (str): name of the page object status property;
                the property should return only bool, not string
            message (str): error message
        """
        message = message or '%s: status is "%s"' % (self.__page_object,
                                                     self.__page_object.status)
        self.__wait.until(lambda self:
                          getattr(self.__page_object, status_prop),
                          message=message)

    def status_not(self, status_prop, message=None):
        """
        Waits until page object property `status_prop` is evaluated as False.

        Parameters:
            status_prop (str): name of the page object status property;
                the property should return only bool, not string
            message (str): error message
        """
        message = message or '%s: status is "%s"' % (self.__page_object,
                                                     self.__page_object.status)
        self.__wait.until_not(lambda self:
                              getattr(self.__page_object, status_prop),
                              message=message)
