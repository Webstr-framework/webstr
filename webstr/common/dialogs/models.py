"""
Page models for common dialogs.

Author: pnovotny, ltrilety, mkudlej
"""

# Copyright 2016 Red Hat
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from webstr.core import WebstrModel, PageElement, By, RootPageElement
from webstr.common.form import models


class ModalDlg(WebstrModel):
    """ Base page model for modal dialogs. """
    background_veil = PageElement(By.CSS_SELECTOR, 'div.gwt-PopupPanelGlass')


class CloseDlg(ModalDlg):
    """
    Base page model for dialog window containing 'Close' button.
    This is only a place holder class! Required page elements
    `close_btn` must be defined in all derived page models.
    """


class OkCancelDlg(ModalDlg):
    """
    Base page model for dialog window containing 'OK' and 'Cancel' buttons.
    This is only a place holder class! Required page elements
    `ok_btn` and `cancel_btn` must be defined in all derived page models.
    """


class RemoveConfirmDlg(OkCancelDlg):
    """ Page model for common removal confirmation dialog. """
    ok_btn = models.Button(By.XPATH, '//div[@id="RemoveConfirmationPopupView_OnRemove"]')
    cancel_btn = models.Button(By.XPATH, '//div[@id="RemoveConfirmationPopupView_Cancel"]')


class ErrorDialog(CloseDlg):
    """ dialog with error message model """
    _root = RootPageElement(by=By.XPATH, locator='//div[@class="gwt-DialogBox dialogBoxStyle"]')
    close_btn = models.Button(By.XPATH, '//div[@role="button"][contains(., "Close")]')
    error = PageElement(By.XPATH, '//div[@class="gwt-HTML"]')
