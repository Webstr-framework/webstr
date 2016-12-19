"""
Page models for patternfly Tabs

* https://www.patternfly.org/widgets/#tabs
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
