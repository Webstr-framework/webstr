# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Page model for patternfly/bootstrap modal window.

Modal window is a window which makes itself the only active element on the
page, so that one needs to close it first to access the rest of the page again.
"""


from raut.core import By
from raut.core import PageElement
from raut.core import PageModel
from raut.core import RootPageElement


class ModalWindow(PageModel):
    """
    Base page model class for any modal window.
    """
    _root = RootPageElement(by=By.XPATH, locator="//div[@class='modal-dialog']")
    header= PageElement(by=By.XPATH, locator=".//div[contains(@class, 'modal-header')]")
    body = PageElement(by=By.XPATH, locator=".//div[contains(@class, 'modal-body')]")
    footer = PageElement(by=By.XPATH, locator=".//div[contains(@class, 'modal-footer')]")
    # we expect that the title is always there
    title = PageElement(by=By.XPATH, locator=".//*[contains(@class, 'modal-title')]")
    # there is always a close button (in the right side of the header)
    close_btn = PageElement(by=By.XPATH, locator=".//button[@class='close']")
    # if there are more buttons available in a footer or a body of a modal window
    # you need to define them all in a subclass
