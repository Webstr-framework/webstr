# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Page objects for patternfly/bootstrap modal window.

Modal window is a window which makes itself the only active element on the
page, so that one needs to close it first to access the rest of the page again.
"""


from raut.core import PageObject
from raut.lib.selenium.ui.patternfly.models import modal as m_modal


class ModalWindow(PageObject):
  """
  Base page object class for any modal window.
  """
  _model = m_modal.ModalWindow
  _required_elems = ['header', 'body', 'footer', 'title', 'close_btn']

  def close(self):
    """
    Close the modal windown via default close button in the deader
    (a button labeled "X" in the top right corner).
    """
    self._model.close_btn.click()

  def get_title(self):
    return self._model.title.text
