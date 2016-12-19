"""
Page models for patternfly dropdown menu.
https://www.patternfly.org/widgets/#dropdowns

Author: ltrilety
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


from webstr.core import WebstrModel, DynamicWebstrModel, PageElement, By, RootPageElement, NameRootPageElement


class DropDownMenuRow(DynamicWebstrModel):
    """
    Base class model for drop down menu item.
    """
    _root = NameRootPageElement(by=By.XPATH, locator='./li//ul/li[%d]')


class DropDownMenu(WebstrModel):
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
