"""
Page objects for common dialogs.

Author: pnovotny, ltrilety, mkudlej
"""

from webstr.core import WebstrPage
from webstr.common import timeouts
from webstr.common.models import dialogs as m_dialogs
from webstr.selenium.ui.support import WebDriverWait


class ModalDlg(WebstrPage):
    """
    Base new-style page object for all modal dialogs.
    """
    _timeout = timeouts.MODAL_DIALOG
    _model = m_dialogs.ModalDlg

    def wait_to_disappear(self, timeout=timeouts.MODAL_DIALOG_CLOSE):
        """
        Wait `timeout` seconds until the dialog disappears.

        Parameters:
            timeout - timeout in seconds
        """
        WebDriverWait(self, timeout).until_not(
          lambda self: self._model.background_veil,
          "%s: timeout (%d seconds) expired. "
          "Dialog window is still present." % (self.__class__.__name__, timeout))


class CloseDlg(ModalDlg):
    """
    Abstract base page object for new-style dialog windows
    containing 'Close' button.

    Note, that this page object implements only functionality
    for the OK & Cancel buttons. The button page elements must be defined
    in particular page model of the derived page object class.
    """
    _model = m_dialogs.CloseDlg
    _label = 'OK/Cancel dialog'
    _required_elems = ['close_btn']

    def close(self):
        """
        Close dialog, hit the close button

        Return: True
        """
        self._model.close_btn.click()

    def close_and_wait_to_disappear(self, timeout=timeouts.MODAL_DIALOG_CLOSE):
        """
        Submit dialog and wait until all dialog windows disappear.

        Caution: use only if you are sure, that after the dialog
        has been submitted, no other or new dialog windows are present!

        Parameters:
            timeout - number of seconds to wait until the window disappears
        Return: True - success
        """
        self.close()
        self.wait_to_disappear(timeout)
        return True


class OkCancelDlg(ModalDlg):
    """
    Abstract base page object for new-style dialog windows
    containing 'OK' and 'Cancel' buttons.

    Note, that this page object implements only functionality
    for the OK & Cancel buttons. The button page elements must be defined
    in particular page model of the derived page object class.
    """
    _model = m_dialogs.OkCancelDlg
    _label = 'OK/Cancel dialog'
    _required_elems = ['ok_btn', 'cancel_btn']

    def submit(self):
        """
        Submit dialog - just click on 'OK' button.
        Return: True
        """
        self._model.ok_btn.click()
        return True

    def submit_and_wait_to_disappear(self, timeout=timeouts.MODAL_DIALOG_CLOSE):
        """
        Submit dialog and wait until all dialog windows disappear.

        Caution: use only if you are sure, that after the dialog
         has been submitted, no other or new dialog windows are present!

        Parameters:
            timeout - number of seconds to wait until the window disappears
        Return: True - success
        """
        self.submit()
        self.wait_to_disappear(timeout)
        return True

    def cancel(self):
        """
        Cancel popup - click on 'Cancel' button.

        Return: True
        """
        self._model.cancel_btn.click()
        return True


class RemoveConfirmDlg(OkCancelDlg):
    """New-style page object for removal confirmation dialogs."""
    _model = m_dialogs.RemoveConfirmDlg


class ErrorDialog(CloseDlg):
    """Profiling pop up menu"""
    _model = m_dialogs.ErrorDialog
    _label = "Error dialog"

    @property
    def error(self):
        """Get error text"""
        return self._model.error.text
