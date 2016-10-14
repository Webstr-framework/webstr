"""
WebDriver module providing extended functionality via WebDriverExtension class.

Multiple inheritance is used to avoid defining helper methods
in all browser driver classes.

.. moduleauthor:: pnovotny
"""

import base64
import logging
import tempfile
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.common import exceptions as selenium_ex

from webstr.selenium.webelement import FreshWebElement
from webstr.core import config


LOGGER = logging.getLogger(__name__)


class WebDriverExtension(object):
    """
    WebDriver extension providing additional functionality.
    """

    def _parse_ui_map_locator(self, locator):
        """
        Parse given ui locator, which must be a 2-item tuple, where
        first item is locator type (see :class:`selenium.webdriver.common.by.By`)
        and second is locator value,
        e.g., `(By.ID, 'LoginPopupView_userName')`.

        Parameters:
            locator (2 item tuple): 1st item is locator type, 2nd item is value

        Returns: 2-item tuple
        Throws: ValueError - parsing failed
        """
        try:
            locator_type = locator[0]
            locator_value = locator[1]
        except (IndexError, TypeError):
            raise ValueError("A tuple with two elements is required "
                             "but '%s' given." % locator)
        return (locator_type, locator_value)

    def find_element(self, by, value, auto_refresh=True):
        """
        Overrides webdriver's method `find_element`.
        If `auto_refresh` is True, then returns FreshWebElement instance,
        otherwise the regular WebElement.

        Parameters:
            by (str): location method
            value (str): locator value
            auto_refresh (bool): True - return FreshWebElement (default),
                otherwise WebElement instance
        """
        elem = super(WebDriverExtension, self).find_element(by=by, value=value)
        if not auto_refresh:
            return elem
        return FreshWebElement(element=elem, by=by, value=value)

    def find_elements(self, by, value, auto_refresh=True):
        """
        Overrides webdriver's method `find_elements`.
        If `auto_refresh` is True, then returns list of FreshWebElement
        instances, otherwise regular list of WebElement instances.

        Parameters:
            by (str): location method
            value (str): locator value
            auto_refresh (bool): True - return FreshWebElement (default),
                otherwise WebElement instance
        """
        elems = super(WebDriverExtension, self).find_elements(by=by,
                                                              value=value)
        if not auto_refresh:
            return elems
        return [FreshWebElement(element=elem, by=by, value=value) for
                elem in elems]

    def find_element_by_ui_map(self, locator):
        """
        Find element by UI map.

        Parameters:
            locator (2 item tuple): 1st item is locator type, 2nd item is value
        Return: WebElement instance
        """
        locator_type, locator_value = self._parse_ui_map_locator(locator)
        return self.find_element(by=locator_type, value=locator_value)

    def find_elements_by_ui_map(self, locator):
        """
        Find elements by UI map.

        Parameters:
            locator - 2-tuple; 1st item is locator type, 2nd item is value
        Return: list of WebElement instance(s)
        """
        locator_type, locator_value = self._parse_ui_map_locator(locator)
        return self.find_elements(by=locator_type, value=locator_value)

    def get_screen_filename(self, prefix=None, suffix=None,
                            use_timestamp=True):
        """
        Create temporary file and return its filename.

        Parameters:
           suffix: file suffix
           prefix: file prefix
           use_timestamp: True/False; append timestamp to file prefix
        Return: filename (including full path)
        """
        screen_prefix = prefix or 'Selenium-screen'
        screen_suffix = suffix or '.png'
        directory = '.'
        if use_timestamp:
            screen_prefix = ''.join(
              (screen_prefix, '-%s-' % time.strftime("%Y-%m-%d_%H-%M-%S")))
        return tempfile.mkstemp(
          prefix=screen_prefix, suffix=screen_suffix, dir=directory)[1]

    def save_screen_as_file(self, filename=None):
        """
        Save the screenshot of the current window.

        Parameters:
            filename - the full path you wish to save your screenshot to
        Return: filename - success / False - error (IOError)
        """
        filename = filename or self.get_screen_filename()
        if self.get_screenshot_as_file(filename):
            return filename
        return False

    def __save_screen_on_except(self, exception):
        """
        Save screenshot returned in risen WebDriver exception.

        Parameters:
            exception: exception instance
        Return: True - success / False - error or no screenshot to save
        """
        try:
            if exception.screen:
                try:
                    filename = self.get_screen_filename()
                    with open(filename, 'wb') as fileh:
                        fileh.write(base64.decodestring(exception.screen))
                    LOGGER.info("Screenshot saved: %s (%d bytes)",
                                filename, len(exception.screen))
                except IOError as ex:
                    LOGGER.error("Failed to save screenshot: %s", ex)
                    return False
        except AttributeError:
            return False
        return True


class Firefox(WebDriverExtension, webdriver.Firefox):
    """
    Extended Firefox driver.
    """

    def __init__(self, **params):
        """
        Calling original Firefox init.
        """
        super(Firefox, self).__init__(**params)


class Chrome(WebDriverExtension, webdriver.Chrome):
    """
    Extended Chrome driver.
    """

    def __init__(self, **params):
        """
        Calling original Chrome init.
        """
        super(Chrome, self).__init__(**params)


class Ie(WebDriverExtension, webdriver.Ie):
    """
    Extended IE driver.
    """

    def __init__(self, **params):
        """
        Calling original IE init.
        """
        super(Ie, self).__init__(**params)


class Remote(WebDriverExtension, webdriver.Remote):
    """
    Extended Remote driver.
    """
    PAGE_LOAD_TIMEOUT = 20

    def __init__(self, **params):
        """
        Calling original Remote init.
        """
        super(Remote, self).__init__(**params)

    @property
    def __is_ie(self):
        """Returns whether the driver instance is IE or not."""
        return self.name in DesiredCapabilities.INTERNETEXPLORER['browserName']

    def __ie_confirm_cert_exception(self):
        """
        Tries to automatically confirm the notorious IE "Certificate Error"
        warning page.
        Note that the JS command is called via `get` method,
        because `execute_script` does not work in this case for some reason.
        """
        js_cmd = "javascript:document.getElementById('overridelink').click();"
        try:
            self.set_page_load_timeout(1)
            super(Remote, self).get(js_cmd)
        except selenium_ex.TimeoutException:
            # "Certificate Error" page is not present, moving on
            pass
        finally:
            self.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)

    def get(self, *args, **kwargs):
        """
        Overridden method. Loads a URL and automatically confirms
        possible HTTPS certificate error warning (for IE only).
        """
        super(Remote, self).get(*args, **kwargs)
        if self.__is_ie:
            self.__ie_confirm_cert_exception()


class DriverFactory(object):
    """
    WebDriver instance factory.

    Attributes:
        __driver_map_local (dict): mapping of local WebDriver classes
            according to the browser name
        __desired_capabilities_map (dict): mapping of desired capabilities
            according to the browser name
    """
    __driver_map_local = {'Firefox': Firefox,
                          'Chrome': Chrome,
                          'Internet Explorer': Ie}
    __desired_capabilities_map = {'Firefox': DesiredCapabilities.FIREFOX,
                                  'Chrome': DesiredCapabilities.CHROME,
                                  'Internet Explorer':
                                    DesiredCapabilities.INTERNETEXPLORER}

    def __new__(cls, browser_name, host=None, port=None,
                desired_capabilities=None, **kwargs):
        """
        Return WebDriver instance of desired browser.

        If host and port are specified, remote WebDriver is created,
        otherwise local WebDriver instance is returned.

        Parameters:
            browser_name (str): browser name
            host (str): webdriver server FQDN/IP; remote driver only
            port (int): webdriver server port; remote driver only
            desired_capabilities (dict): browser desired capabilities;
                Use the same format and keys as in DesiredCapabilities.*;
                remote driver only
        Return: local or remote WebDriver instance
        """
        if host and port:
            return cls.__get_remote_driver(
              browser_name, host, port, desired_capabilities, **kwargs)
        return cls.__get_local_driver(browser_name, **kwargs)

    @classmethod
    def __get_remote_driver(cls, browser_name, host, port,
                            desired_capabilities=None, **kwargs):
        """
        Return remote WebDriver instance.

        Parameters: see `__new__()`
        Return: <Remote> WebDriver instance
        Throws: KeyError - wrong browser name
        """
        command_executor = RemoteConnection(
          'http://%s:%s/wd/hub' % (host, port))
        try:
            capabilities = cls.__desired_capabilities_map[browser_name].copy()
        except KeyError as ex:
            ex.args = ("unknown browser: '%s' (valid browsers: %s)"\
              % (browser_name, ', '.join(cls.__desired_capabilities_map.keys())),)
            raise ex
        if desired_capabilities:
            capabilities.update(desired_capabilities)

        return Remote(command_executor=command_executor,
                      desired_capabilities=capabilities,
                      **kwargs)

    @classmethod
    def __get_local_driver(cls, browser_name, **kwargs):
        """
        Return local WebDriver instance.

        Parameters: see `__new__()`
        Return: local WebDriver instance
        Throws: KeyError - wrong browser name
        """
        try:
            driver_cls = cls.__driver_map_local[browser_name]
        except KeyError as ex:
            ex.args = ("unknown browser: '%s' (valid browsers: %s)"\
              % (browser_name, ', '.join(cls.__driver_map_local.keys())),)
            raise ex
        driver = driver_cls(**kwargs)
        driver.set_window_size(config.BROWSER_WIDTH, config.BROWSER_HEIGHT)
        return driver
