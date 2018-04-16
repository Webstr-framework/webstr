"""
Page models for patternfly Content Views:

* https://www.patternfly.org/list-view/
* https://www.patternfly.org/patterns/table-view/
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


class ListViewModel(WebstrModel):
    """
    A List View displays data in rows. Each row displays the same set of
    attributes, although not necessarily displayed in columns, and the
    attributes may wrap.

    See: https://www.patternfly.org/list-view/

    Note: we are interested only for the list view presented in the correct container hence
          //*[contains(@class, "col-md-12")]
    """
    LIST_XPATH = '//*[contains(concat(" ", @class, " "), " list-view-pf ")]'
    _root = RootPageElement(By.XPATH, LIST_XPATH)
    rows = PageElement(
      by=By.XPATH,
      locator=LIST_XPATH + "//*[contains(concat(' ', @class, ' '), ' list-group-item ')]",
      as_list=True)


class ListViewRowModel(DynamicWebstrModel):
    """
    Item/row of a List View
    """
    _root = NameRootPageElement(
      by=By.XPATH,
      locator='(' + ListViewModel.LIST_XPATH + '//*[contains(concat(" ", @class, " "), " list-group-item ")])[%d]')


class TableViewModel(WebstrModel):
    """
    The table view organizes data into rows (of items) and columns (of item
    attributes).

    See: https://www.patternfly.org/patterns/table-view/
    """

    TABLE_XPATH = '//table[contains(concat(" ", @class, " "), " table ")]'
    _root = RootPageElement(By.XPATH, TABLE_XPATH)
    rows = PageElement(
      by=By.XPATH,
      locator=TABLE_XPATH + "//tr",
      as_list=True)


class TableViewRowModel(DynamicWebstrModel):
    """
    Item/row of a Table View
    """
    _root = NameRootPageElement(
      by=By.XPATH,
      locator='(' + TableViewModel.TABLE_XPATH + '//tr[%d]')
