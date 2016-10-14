"""
Page models for common dialogs.

Author: pnovotny, ltrilety, mkudlej
"""

from webstr.core import WebstrModel, PageElement, By, RootPageElement
from webstr.lib.selenium.ui.common.models import form


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
    ok_btn = form.Button(By.XPATH, '//div[@id="RemoveConfirmationPopupView_OnRemove"]')
    cancel_btn = form.Button(By.XPATH, '//div[@id="RemoveConfirmationPopupView_Cancel"]')


class ErrorDialog(CloseDlg):
    """ dialog with error message model """
    _root = RootPageElement(by=By.XPATH, locator='//div[@class="gwt-DialogBox dialogBoxStyle"]')
    close_btn = form.Button(By.XPATH, '//div[@role="button"][contains(., "Close")]')
    error = PageElement(By.XPATH, '//div[@class="gwt-HTML"]')
