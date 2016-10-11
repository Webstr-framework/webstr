# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Page models for common action popup panels.

Author: ltrilety
"""

from raut.core import PageModel, RootPageElement, By
from raut.lib.selenium.ui.common.models import form


class ActionPopupPanel(PageModel):
  """ Base Action Pop Up Panel model """
  _root = RootPageElement(By.CLASS_NAME, "actionPanelPopupPanel")

  status_btn = form.Button(By.XPATH, '//div[@class="actionPanelPopupPanel"]//td[contains(text(), "Status")]')
  stop_btn = form.Button(By.XPATH, '//div[@class="actionPanelPopupPanel"]//td[contains(text(), "Stop")]')
