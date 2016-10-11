# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Page models for patternfly dropdown menu.
https://www.patternfly.org/widgets/#dropdowns

Author: ltrilety
"""

from raut.core import PageModel, DynamicPageModel, PageElement, By, RootPageElement, NameRootPageElement


class DropDownMenuRow(DynamicPageModel):
    """
    Base class model for drop down menu item.
    """
    _root = NameRootPageElement(by=By.XPATH, locator='./li//ul/li[%d]')


class DropDownMenu(PageModel):
    """ Base page model for any active dropdown menu.
    NOTE for drop down menu on admin-users page for any user it can be iterated right away any <li> element is a row
         for tasks the iterable part is deeper in another <ul> element or them there's UpperDropDownMenu class
    """
    _base_locator = '//*[contains(@class, "dropdown-menu")][contains(@class, "ng-scope")]/..'
    _root = RootPageElement(by=By.XPATH, locator=_base_locator + '/ul[./li]')
    rows = PageElement(By.XPATH, './li', as_list=True)

# TODO: consider UpperDropDownMenuRow (including related page class)

class UpperDropDownMenu(DropDownMenu):
    """ Page model for dropdowns menu presented in upper menu """
    _root = RootPageElement(by=By.XPATH, locator=DropDownMenu._base_locator + '/ul[./li//ul]')
    rows = PageElement(By.XPATH, './li//ul/li', as_list=True)
