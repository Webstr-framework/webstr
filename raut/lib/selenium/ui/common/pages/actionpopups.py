# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Page objects for common dialogs.

Author: ltrilety
"""

from raut.core import PageObject
from raut.lib.selenium.ui.common import timeouts
from raut.lib.selenium.ui.common.models import actionpopups as m_actionpopups


class ActionPopupPanel(PageObject):
  """Base Action Pop Up Panel"""
  _model = m_actionpopups.ActionPopupPanel
  _timeout = timeouts.POPUP_WINDOW
  _reqired_elems = ['status_btn', 'stop_btn']

  def hit_stop_btn(self):
    """Hit stop button"""
    self._model.stop_btn.click()

  def hit_status_btn(self):
    """Hit status button"""
    self._model.status_btn.click()
