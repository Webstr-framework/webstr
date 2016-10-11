"""
Page models for patternfly Content Views:

* https://www.patternfly.org/list-view/
* https://www.patternfly.org/patterns/table-view/
"""

from raut.core import By, DynamicPageModel, PageElement, PageModel, RootPageElement, NameRootPageElement


class ListView(PageModel):
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


class ListViewRow(DynamicPageModel):
    """
    Item/row of a List View
    """
    _root = NameRootPageElement(
      by=By.XPATH,
      locator='(' + ListView.LIST_XPATH + '//*[contains(concat(" ", @class, " "), " list-group-item ")])[%d]')


class TableView(PageModel):
    """
    The table view organizes data into rows (of items) and columns (of item
    attributes).

    See: https://www.patternfly.org/patterns/table-view/
    """

    # TODO
