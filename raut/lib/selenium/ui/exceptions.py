# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
General UI-related exceptions module.

Make sure all user-defined exception inherits from GeneralException!

Author: pnovotny
"""

class GeneralException(Exception):
  """Base class for user defined exceptions."""
  message = "General Exception"

  def __init__(self, *value):
    self.value = value

  def _value_repr(self):
    return repr(self.value[0] if len(self.value) == 1 else self.value)

  def __str__(self):
    return "%s: %s" % (self.message, self._value_repr())

  def __repr__(self):
    return "%s(%s: %s)" % (self.__class__.__name__, self.message, self._value_repr())


class InitPageValidationError(GeneralException):
  """
  Initial validation error upon PageObject creation.
  """
  message = "Initial page validation error"


class UserActionError(GeneralException):
  """
  Base error class for all user action related errors.
  """
  message = "user action failed"


class FieldIsRequiredError(UserActionError):
  """
  Required input field is not filled.
  Input field can be input text, select box, radio button, etc.
  """
  message = "Field is required"


class LoginError(UserActionError):
  """
  Invalid username or password provided.
  """
  message = "Login Failed"


class ElementDoesNotExistError(GeneralException):
  """
  Element does not exist.
  """
  message = "element does not exist"


class WaitTimeoutError(GeneralException):
  """
  Wait timeout expired.
  """
  message = "timeout expired"


class NoSuchRowException(GeneralException):
  """
  the row does not exist
  """
  message = "The row does not exist in the table"
