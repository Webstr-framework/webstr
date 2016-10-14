"""
Page models for patternfly Tabs

* https://www.patternfly.org/widgets/#tabs
"""

from webstr.core import By, DynamicWebstrModel, PageElement, WebstrModel, RootPageElement, NameRootPageElement


class Tabs(WebstrModel):
    """
    Tabs allow to display more pages at one place by changing tab.

    See: https://www.patternfly.org/widgets/#tabs
    """
    TABS_XPATH = '//ul[contains(@class,"nav nav-tabs")]'
    _root = RootPageElement(By.XPATH, TABS_XPATH)
    tabs = PageElement(
      by=By.XPATH,
      locator=TABS_XPATH + "/li/a",
      as_list=True)


class Tab(DynamicWebstrModel):
    """
    Item/tab of a Tabs
    """
    _root = NameRootPageElement(
      by=By.XPATH,
      locator=Tabs.TABS_XPATH + '/li/a[contains(text(),%s)]')