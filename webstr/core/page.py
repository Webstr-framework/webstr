"""
Base design of page objects.

Author: pnovotny
"""

from selenium.common import exceptions as selenium_ex

from webstr.core import WebstrModel, DynamicWebstrModel
from webstr.selenium.ui import exceptions as ui_exceptions
from webstr.common import timeouts


class WebstrPageBase(object):
    """
    base class for page object.

    Parameters:
        _driver: Selenium webdriver instance
        _location: default page location; optional
                   if None, no URL is loaded after object initialization
        _timeout: implicit timeout in [s] for all page object instances
        _model: page object model instance (enumerator of page elements
                and related strings)
        _label: human-readable label used for PO string representation
        _required_elems: which web elements will be checked during init validation run
    """
    _driver = None
    _location = None
    _timeout = timeouts.PAGE_OBJECT
    _model = None
    _label = None
    _required_elems = None

    def __init__(self, driver, **kwargs):
        """
        Init, set implicit timeout for element search, load URL if one is given
          and run init validation, ensuring that we are on the right location.

        Parameters:
            * driver - webdriver instance
            * kwargs - additional arguments, which are passed to <init> method
        """
        self._driver = driver
        self._driver.implicitly_wait(self._timeout)
        if self._location:
            self._driver.get(self._location)
        self.init(**kwargs)
        self._initial_page_object_validation()

    def __str__(self):
        """ Return human readable page object label if available. """
        return self._label or '<%s> page object' % self.__class__.__name__

    def __unicode__(self):
        return unicode(str(self))

    def _initial_page_object_validation(self):
        """
        Calls <init_validation> method and reports all WebDriver
        and ElementDoesNotExistError exceptions
        as page object validation error.
        """
        try:
            self.init_validation()
        except (selenium_ex.WebDriverException,
                ui_exceptions.ElementDoesNotExistError) as ex:
            raise ui_exceptions.InitPageValidationError(
              "could not initialize %s within %d seconds; reason: %s" % (self, self._timeout, ex))

    @property
    def driver(self):
        """
        WebDriver instance property.
        Return: self._driver
        """
        return self._driver

    @property
    def location(self):
        """
        Page URL property, mostly used for initial loading the page.
        Return: self._location
        """
        return self._location

    def init(self, **kwargs):
        """
        Process additional arguments passed from __init__.
          This method can be overloaded in descendant class
          for its specific purpose.
        Parameters:
            * kwargs - additional arguments passed from __init__
        """

    def init_validation(self):
        """
        Initial page object validation.
        It check if all elements in _required_elems list are present.
        This method is always called at the end of the __init__ method.
        Note: All WebDriverException errors in this method are caught
        automatically and an InitPageValidationError is thrown in return.
        Other types of exceptions must be caught explicitly.
        Throws: should be an InitPageValidationError in case of error
        """
        if self._required_elems is None:
            raise NotImplementedError('_required_elems list has to be defined')
        for elem in self._required_elems:
            getattr(self._model, elem)

    @property
    def is_present(self):
        """ return whether the page object is present or not.
        the page object presence is determined by running
        the initial validation routine.
        return: True - is present / False - not present
        """
        try:
            self._initial_page_object_validation()
        except ui_exceptions.InitPageValidationError:
            return False
        return True

    def get_model_element(self, model_attr_name):
        """
        Return page element available in this page's model.

        This is a hack which allows you to write somewhat working code quickly,
        but I would suggest to not use this much in the final version.

        Returns:
            Page element from the model.
            None if there is no `model_attr_name` attribute in the model.
        """
        try:
            return self._model.__getattribute__(model_attr_name)
        except AttributeError as ex:
            # TODO: this is not a good idea, remove this later
            return None


class WebstrPage(WebstrPageBase):
    """
    New-style static page object.
    """

    def __init__(self, driver):
        """
        Initialize the page object and check the page model class is valid.

        Parameters:
            * driver - webdriver instance
        """
        if not issubclass(self._model, WebstrModel):
            raise TypeError("page model type mismatch: "
                            "%s class is not subclass of WebstrModel"
                            % self._model.__name__)
        self._model = self._model(driver)
        super(WebstrPage, self).__init__(driver)


class DynamicWebstrPage(WebstrPageBase):
    """
    New-style dynamic page object.
    All dynamic page object instances must specify its name, according to whose
    it's possible to identify it.

    Usage:
      class VMInstance(DynamicWebstrPage):
          ...
          ...

      vm_instance = VMInstance(driver, name='test-vm-01')
    """

    def __init__(self, driver, name):
        """
        Initialize the page object and check the page model class is valid.

        Parameters:
            * driver - webdriver instance
            * name - page object name; this value is also passed
               to the dynamic page model initiator as its instance identifier.
        """
        self._name = name
        self._label = '%s %s' % (self._label, name)
        if not issubclass(self._model, DynamicWebstrModel):
            raise TypeError("page model type mismatch: "
                            "%s class is not subclass of DynamicWebstrModel"
                            % self._model.__name__)
        self._model = self._model(driver, name)
        super(DynamicWebstrPage, self).__init__(driver)
