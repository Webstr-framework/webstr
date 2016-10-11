# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Selenium WebDriver instance manager.

.. moduleauthor:: pnovotny
"""

from raut.core import config
from raut.lib.selenium.webdriver import DriverFactory


class Driver(object):
  """WebDriver instance manager & cache."""
  __driver = None

  def __new__(cls):
    """
    Raises:
        NotImplementedError - if someone wants to instantiate this class
    """
    raise NotImplementedError("for instance creation use factory method: "
                              "driver = Driver.get_default_driver()")

  @classmethod
  def get_default_driver(cls):
    """
    Factory method, creates :class:`WebDriver` instance according
    to configuration parameters or returns existing one,
    if called multiple times.

    Returns:
        :class:`WebDriver` instance
    """
    if cls.__driver:
      return cls.__driver

    capabilities = {
      'platform': config.BROWSER_PLATFORM,
      'version': str(config.BROWSER_VERSION),
      }
    cls.__driver = DriverFactory(browser_name=config.BROWSER,
                                 host=config.SELENIUM_SERVER,
                                 port=config.SELENIUM_PORT,
                                 desired_capabilities=capabilities)
    return cls.__driver

  @classmethod
  def destroy_default_driver(cls):
    """
    Remove the cached driver instance, if exists.
    This step is necessary for replacing the cached driver instance with
    new one via :func:`get_default_driver()`.
    """
    cls.__driver = None
