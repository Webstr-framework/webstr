"""
.. module:: core
   :synopsis: Shortcut imports for commonly used functionality.

.. moduleauthor:: Pavel Novotny <pnovotny@redhat.com>
"""

from selenium.webdriver.common.by import By
from webstr.core.model import(
    WebstrModel, DynamicWebstrModel, BaseWebElementHelper,
    PageElement, DynamicPageElement, RootPageElement, NameRootPageElement
) # flake8: noqa
from webstr.core.page import(WebstrPage, DynamicWebstrPage)
