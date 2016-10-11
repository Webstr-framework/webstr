# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
.. module:: core
   :synopsis: Shortcut imports for commonly used functionality.

.. moduleauthor:: Pavel Novotny <pnovotny@redhat.com>
"""

from selenium.webdriver.common.by import By
from raut.core.pagemodel import(
    PageModel, DynamicPageModel, BaseWebElementHelper,
    PageElement, DynamicPageElement, RootPageElement, NameRootPageElement
) # flake8: noqa
from raut.core.pageobject import(PageObject, DynamicPageObject)
