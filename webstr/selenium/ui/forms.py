"""
Widget helpers for HTML form elements.

Author: pnovotny
"""

from selenium.common import exceptions as selenium_ex
from selenium.webdriver.support.ui import Select as _SelectBase

from webstr.core import By, BaseWebElementHelper


class Checkbox(BaseWebElementHelper):
    """
    Checkbox helper (Selenium webelement wrapper).
    Provides basic methods for manipulation of a checkbox widget.
    """

    def __init__(self, webelement):
        """
        Parameters:

            webelement - element to wrap

        Throws: UnexpectedTagNameException - element tag name is not 'INPUT'
        """
        super(Checkbox, self).__init__(webelement)
        if webelement.tag_name != "input":
            raise selenium_ex.UnexpectedTagNameException(
              "Checkbox only works on <input> elements, not on <%s>" % webelement.tag_name)

    @property
    def value(self):
        """
        Return whether checkbox is checked or unchecked.

        Returns:
            True - checked / False - unchecked
        """
        return self.is_checked

    @property
    def is_checked(self):
        """
        Return whether checkbox is checked or unchecked.

        Returns:
            True - checked / False - unchecked
        """
        return self._elem.is_selected()

    @value.setter
    def value(self, value):
        """
        Setter method for handling the widget when using value assignment.

        Parameters:
            value:
                value used in assignment
                options: True - check; False - uncheck; None - do nothing
        """
        self.do_check(value)

    def check(self):
        """Check the checkbox."""
        if not self.is_checked:
            self._elem.click()

    def uncheck(self):
        """Uncheck the checkbox."""
        if self.is_checked:
            self._elem.click()

    def do_check(self, to_check):
        """
        Check or uncheck checkbox according to boolean expression parameter.

        Parameters:
            to_check (boolean): True - check, False - uncheck, None - do nothing
        """
        if to_check is not None:
            if to_check:
                self.check()
            else:
                self.uncheck()


class Select(_SelectBase):
    """A SELECT element wrapper with extended functionality."""

    @property
    def value(self):
        """
        Getter method for getting selected option text

        Returns:
            text of the selected options
        """
        return [elem.text for elem in self.all_selected_options]

    @value.setter
    def value(self, value):
        """
        Setter method for handling the widget when using value assignment.

        Parameters:
            value:
                value used in assignment
        """
        self.select_by_value(str(value))

    def select_by_value_starting_with(self, value):
        """
        Select all options that have a value starting with the `value` argument.

        That is, when given "foo" this would select options like::

            <option value="foo">Bar</option>
            <option value="foo_bar">Bar</option>
            <option value="foo (Bar)">Bar</option>

        Note: this method is just modified re-implementation of the original
        `Select.select_by_value` method.

        Parameters:
            value (str): start of the value string to match against
        """
        css = "option[value^=%s]" % self._escapeString(value)
        opts = self._el.find_elements(By.CSS_SELECTOR, css)
        matched = False
        for opt in opts:
            self._setSelected(opt)
            if not self.is_multiple:
                return
            matched = True
        if not matched:
            raise selenium_ex.NoSuchElementException(
              "Cannot locate option starting with value: %s" % value)

    def select_by_visible_text_starting_with(self, text):
        """
        Select all options that the display text starts with the `text` argument.

        That is, when given "Bar" this would select options like:

            <option value="foo">Bar</option>
            <option value="foo">BarBaz</option>
            <option value="foo"> Bar (Baz)</option>

        Note: this method is just modified re-implementation of the original
        `Select.select_by_visible_text` method.

        Parameters:
            text (str): start of the visible text to match against
        """
        xpath = (".//option[starts-with(normalize-space(.), %s)]"
                 % self._escapeString(text))
        opts = self._el.find_elements(By.XPATH, xpath)
        matched = False
        for opt in opts:
            self._setSelected(opt)
            if not self.is_multiple:
                return
            matched = True

        if not matched:
            msg = "Could not locate option starting with visible text: %s" % text
            raise selenium_ex.NoSuchElementException(msg)
