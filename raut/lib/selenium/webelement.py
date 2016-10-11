# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Customized Selenium WebElement.

Author: pnovotny
"""

from functools import wraps
import logging
import types

from selenium.common import exceptions as selenium_ex


LOGGER = logging.getLogger(__name__)


class FreshWebElement(object):
    """
    Selenium WebElement proxy/wrapper watching over errors
    due to element staleness.
    """
    __ATTEMPTS = 5
    __STALE_ELEM_MSG = "Detected stale element '%s=%s', refreshing (#%s)..."

    def __init__(self, element, by, value):
        """
        Parameters:
            element (WebElement): page element
            by (str): location method
            value (str): locator value
        """
        self._by = by
        self._value = value
        self._elem = element

    def __dir__(self):
        return list(self.__dict__.keys()) + dir(self._elem)

    def __refresh_element(self):
        """Find the element on the page again."""
        driver = self._elem.parent
        self._elem = driver.find_element(by=self._by,
                                         value=self._value,
                                         auto_refresh=False)

    def __getattr__(self, name):
        """
        Delegates all attribute lookups and method calls to the original
        WebElement and watches for StaleElementReferenceException.
        If caught, the WebElement is "refreshed", i.e., it's looked up
        on the page again and the attribute lookup or (decorated) method call
        is executed again on the "fresh" element.
        """
        for attempt in range(1, self.__ATTEMPTS + 1):
            try:
                attr = getattr(self._elem, name)
                break
            except selenium_ex.StaleElementReferenceException:
                LOGGER.debug(self.__STALE_ELEM_MSG, self._by,
                             self._value, attempt)
                self.__refresh_element()

        if isinstance(attr, types.MethodType):
            @wraps(attr)
            def safe_elem_method(*args, **kwargs):
                """ safe element """
                for attempt in range(1, self.__ATTEMPTS + 1):
                    try:
                        attr = getattr(self._elem, name)
                        return attr(*args, **kwargs)
                    except selenium_ex.StaleElementReferenceException:
                        LOGGER.debug(self.__STALE_ELEM_MSG, self._by,
                                     self._value, attempt)
                        self.__refresh_element()

            return safe_elem_method
        return attr
