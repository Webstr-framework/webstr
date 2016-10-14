"""
Page models for common action popup panels.

Author: ltrilety
"""

from webstr.core import WebstrModel, RootPageElement, By
from webstr.lib.selenium.ui.common.models import form


class ActionPopupPanel(WebstrModel):
    """ Base Action Pop Up Panel model """
    _root = RootPageElement(By.CLASS_NAME, "actionPanelPopupPanel")

    status_btn = form.Button(By.XPATH, '//div[@class="actionPanelPopupPanel"]//td[contains(text(), "Status")]')
    stop_btn = form.Button(By.XPATH, '//div[@class="actionPanelPopupPanel"]//td[contains(text(), "Stop")]')
