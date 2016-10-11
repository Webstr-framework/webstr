"""
Base design of a page model and page element.

Author: pnovotny, ltrilety
"""

from abc import ABCMeta, abstractproperty

from raut.lib.selenium.webelement import FreshWebElement


class PageModelBase(object):
    """
    Base class for page models.

    A page model is designed as a lower layer for page objects,
    which provides basic functionality over single web page or its area
    by describing its page elements as class attributes.
    Along with page elements, class attributes can specify other information,
    like string constants, etc.

    For usage see :class:`PageElement` docstring.

    Attributes:
        _root: root page element of a page model. If defined,
               all other page elements are looked up relatively to this root element
               (i.e., inside of the root page element).
    """
    _root = None

    def __init__(self, driver):
        """
        Save the webdriver instance to attribute.

        Parameters:
            driver: webdriver instance
        """
        self._driver = driver

    def __str__(self):
        """Return human readable page model representation."""
        return 'page model <%s>' % self.__class__.__name__

    def __unicode__(self):
        return unicode(str(self))

    def __repr__(self):
        return str(self)


class PageModel(PageModelBase):
    """
    Basic (static) page model.

    It doesn't differ from its base class, but is defined separately
    so we can distinguish it from the DynamicPageModel class.
    Static page model contains only static page elements,
    i.e., :class:`PageElement` instances or its direct descendants.
    """

    def __init__(self, driver):
        """
        Save the webdriver instance to attribute.

        Parameters:
            driver: webdriver instance
        """
        super().__init__(driver)


class DynamicPageModel(PageModelBase, metaclass=ABCMeta):
    """
    Dynamic page model.

    Dynamic page model can contain both - static and dynamic - page elements.
    It must implement property method `_instance_identifier`,
    whose return value is used for string interpolation of locators
    of all dynamic elements.
    """

    def __init__(self, driver, name):
        """
        Save the webdriver instance to an attribute.

        Parameters:
            driver: webdriver instance
            name: page model instance name; this name is used for identifying
                  single instance along others, e.g., single VM in the VM list
        """
        super().__init__(driver)
        self._name = name

    def __str__(self):
        """ Return human readable page model representation. """
        return '%s "%s"' \
               % (super(DynamicPageModel, self).__str__(), self._name)

    # we are using DynamicPageModel without any DynamicPageElement in it,
    # hence this method does not to be implemented at all
    # (the original design was that one have to implement this method in a subclass)
    # TODO: revisit this design change later after the current refactoring/cleanup
    @property
    def _instance_identifier(self):
        """
        Page model instance identifier.

        Property method whose return value is used for string interpolation
        of locators of all dynamic elements.
        """


class BasePageElement(object, metaclass=ABCMeta):
    """
    *Property* of a page model representing a page element.
    This class is not meant to be used as it is
    """

    def __init__(self, by, locator):
        """ Init.
        Save locator type and value to attributes.

        Parameters:
            by: element locator type; see selenium.webdriver.common.by.By
            locator: element locator value
        """
        self._by = by
        self._locator = locator

    def __get__(self, model_obj, objtype=None):
        """ Property getter method.
        Not implemented for the BasePageElement
        """
        raise AttributeError("BasePageElement is abstract class, getter is not implemented")

    def __set__(self, model_obj, value):
        """ Property setter method.
        Not implemented for the BasePageElement.
        """
        raise AttributeError("setting value via assignment is not allowed"
                             " for BasePageElement")

    def __delete__(self, model_obj):
        """ Property delete method
        Not implemented for the any page element.
        """
        raise AttributeError("delete is not allowed for page element")


class RootPageElement(BasePageElement):
    """
    *Property* of a page model representing a root page element.
    If is accessed, it returns standard Selenium <WebElement> instance.
    This class is meant to be used only for root page elements of a page model!
    For regular elements of a page model, use <*PageElement> classes
    and successors.

    Usage:
      class LoginPageModel(PageModel):
        _root = RootPageElement(by=By.ID, locator='LoginPopupView_loginForm')
    """

    def __get__(self, model_obj, objtype=None):
        """ Property getter method.
        The return value is what is returned,
        when a <*PageModel> attribute is accessed.

        Parameters:
            model_obj: <*PageModel> instance
            objtype: type of the model_obj

        Returns:
            Selenium <WebElement> instance
        """
        return model_obj._driver.find_element(by=self._by, value=self._locator)


class NameRootPageElement(BasePageElement):
    """
    *Property* of a page model representing a root page element.
    If is accessed, it returns standard Selenium <WebElement> instance.
    This class is meant to be used only for root page elements of a dynamic page model!
    For regular elements of a page model, use <*PageElement> classes
    and successors.

    Usage:
      class LoginPageModel(DynamicPageModel):
        _root = NameRootPageElement(by=By.XPATH, locator='//table/tbody/td[%d]')
    """

    def __get__(self, model_obj, objtype=None):
        """ Property getter method.
        The return value is what is returned,
        when a <*DynamicPageModel> attribute is accessed.

        Parameters:
            model_obj: <*DynamicPageModel> instance
            objtype: type of the model_obj

        Returns:
            Selenium <WebElement> instance
        """
        return model_obj._driver.find_element(by=self._by, value=self._locator % model_obj._name)


class PageElement(RootPageElement):
    """
    *Property* of a page model representing a general page element.
    If it is accessed, it returns standard Selenium <WebElement> instance
    or instance of a wrapper helper class defined as `_helper` attribute.

    Usage::
      class SelectBox(PageElement):
          _helper = selenium.webdriver.support.ui.Select

      class LoginPageModel(PageModel):
          username = PageElement(by=By.ID, locator='LoginPopupView_userName')
          domain = SelectBox(by=By.ID, locator='LoginPopupView_domain')

    Class Attributes:
        _helper:
            helper wrapper class, providing extended functionality
            to a WebElement instance.
            Example: selenium.webdriver.support.ui.Select
        _is_dynamic:
            bool; is part of the locator string dynamic
            and needs to be interpolated? false in this case
    """
    _helper = None
    _is_dynamic = False

    def __init__(self, by, locator, as_list=False):
        """
        Save arguments to attributes.

        Parameters:
            by: element locator type; see selenium.webdriver.common.by.By
            locator: element locator value
            as_list: bool; return single page element or a list of element(s)

        Throws: ValueError - attempt for using a dynamic element as list
        """
        super().__init__(by, locator)
        if self._is_dynamic and as_list:
            raise ValueError("List of page elements cannot be set as dynamic.")
        self._as_list = as_list

    def __get__(self, model_obj, objtype=None):
        """
        Property getter method.
        The return value is what is returned, when a <*PageModel> attribute
        is accessed. If model instance has defined a root element
        (via `_root` attribute), all page elements are looked up
        relatively to the root element.

        Parameters:
            model_obj: <*PageModel> instance
            objtype: type of the model_obj

        Returns:
            Selenium <WebElement> instance or instance of a user-defined helper
        """
        # hack: make sphinx happy (access without an instance)
        if model_obj is None:
            return None

        root_element = model_obj._root or model_obj._driver

        lookup_method = root_element.find_element
        if self._as_list:
            lookup_method = root_element.find_elements

        locator = self._locator
        if self._is_dynamic:
            locator = self._locator % model_obj._instance_identifier

        webelement = lookup_method(by=self._by, value=locator)
        if self._helper:
            return self._helper(webelement)
        return webelement


class DynamicPageElement(PageElement):
    """
    *Property* of a page model representing a general dynamic page element.
    If is accessed, it returns a <WebElement> instance or instance
    of a wrapper helper class defined as `_helper` attribute.
    Dynamic page element suppose to have part(s) of the locator string defined
    for run-time interpolation using the '%s' formatter.

    Usage:
      class VMInstanceModel(DynamicPageModel):
          name = DynamicPageElement(by=By.ID, locator='VMList_name_%s')
          status = DynamicPageElement(by=By.ID, locator='VMList_status_%s')

          def _instance_identifier(self):
              # user-defined action, return value(s) will be used
              # for string interpolation of the locator
              return self._name

      vm_mod = VMInstanceModel(driver, 'test-vm-01')


    Attributes:
        _is_dynamic: bool; is part of the locator string dynamic
                     and needs to be interpolated? true in this case
    """
    _is_dynamic = True

    def __init__(self, by, locator):
        """
        Note that with dynamic page element you cannot return list of elements
        using the `as_list` argument as with static page element.

        Parameters:
            by: element locator type; see selenium.webdriver.common.by.By
            locator: element locator value
        """
        super().__init__(by=by, locator=locator, as_list=False)


class BaseWebElementHelper(FreshWebElement, metaclass=ABCMeta):
    """
    Base helper for PageElement property getter
    """

    def __init__(self, webelement):
        """
        Parameters:
            webelement:
                selenium web element or FreshWebElement
        """
        try:
            self._elem = webelement._elem
            self._value = webelement._value
            self._by = webelement._by
        except AttributeError:
            self._elem = webelement
            self._value = None
            self._by = None

    @abstractproperty
    def value(self):
        """
        Selenium WebElement value property
        """
