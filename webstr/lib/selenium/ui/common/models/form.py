"""
Page elements for basic form widgets.

Author: pnovotny
"""

from webstr.lib.selenium.ui import forms
from webstr.core import PageElement, BaseWebElementHelper


class Checkbox(PageElement):
    """
    Page element for a checkbox widget.
    """
    _helper = forms.Checkbox


class BaseRadio(BaseWebElementHelper):
    """
    Web element wrapper for a radio widget
    """

    @property
    def value(self):
        """
        Getter method returns if radio button is selected
        """
        return self.is_selected()

    @value.setter
    def value(self, value):
        """
        Setter method for handling the widget when using value assignment.

        Parameters:
            value:
                value used in assignment
                options: True expression - select radio; otherwise do nothing
        """
        if value == True:
            self.click()


class Radio(PageElement):
    """
    Page element for a radio widget.
    """
    _helper = BaseRadio


class Button(PageElement):
    """
    Page element for a GWT button widget.
    """


class Select(PageElement):
    """
    Page element for a select box widget.
    """
    _helper = forms.Select


class BaseTextInput(BaseWebElementHelper):
    """
    Web element wrapper for a text input widget.
    """
    @property
    def value(self):
        """
        Getter method returns current text of the element
        """
        return self.get_attribute("value")

    @value.setter
    def value(self, value):
        """
        Setter method for handling the widget when using value assignment.

        Parameters:
            element: Selenium <WebElement> instance
            value: value used in assignment
        """
        self.clear()
        self.send_keys(value)


class TextInput(PageElement):
    """
    Page element for a text input widget.
    """
    _helper = BaseTextInput

PasswordInput = TextInput

TextArea = TextInput


class BaseComboBox(BaseWebElementHelper):
    """
    Web element wrapper for a combo-box widget.

    Class attributes:
        _KEY_ENTER (unicode):
            Enter key representation
            The Selenium's `Keys.ENTER` could not be used because the widget
            didn't react to it, so the classic sequence CRLF was used.
    """
    _KEY_ENTER = u'\r\n'

    @property
    def value(self):
        """
        Getter method returns current text of the element
        """
        return self.text

    @value.setter
    def value(self, value):
        """
        Setter method for handling the widget when using value assignment.
        The value is actually assigned to the inner INPUT element.

        Parameters:
            value (str): value to be assigned
        """
        input_elem = self.find_element_by_tag_name('input')
        input_elem.clear()
        input_elem.send_keys(value)
        input_elem.send_keys(self._KEY_ENTER)


class ComboBox(PageElement):
    """
    Page element for a combo-box widget.
    """
    _helper = BaseComboBox


class DynamicCheckbox(Checkbox):
    """
    Page element for a dynamic checkbox widget.
    """
    _is_dynamic = True


class DynamicRadio(Radio):
    """
    Page element for a dynamic radio widget.
    """
    _is_dynamic = True


class DynamicButton(Button):
    """
    Page element for a dynamic GWT button widget.
    """
    _is_dynamic = True


class DynamicSelect(Select):
    """
    Page element for a dynamic select box widget.
    """
    _is_dynamic = True


class DynamicTextInput(TextInput):
    """
    Page element for a dynamic text input widget.
    """
    _is_dynamic = True


DynamicPasswordInput = DynamicTextInput
