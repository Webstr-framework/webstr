# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Page objects for patternfly Content Views:

* https://www.patternfly.org/list-view/
* https://www.patternfly.org/patterns/table-view/
"""

from raut.core import DynamicPageObject, PageObject
from raut.lib.selenium.ui.patternfly.models import contentviews as m_contentviews
import raut.lib.selenium.ui.common.pages.containers as containers


class ListViewRow(containers.ContainerRowBase):
    """
    Item of a List View.
    """
    _model = m_contentviews.ListViewRow
    _label = 'ListView row'
    _required_elems = ['_root']


class ListView(containers.ContainerBase):
    """
    See: https://www.patternfly.org/list-view/
    """
    _model = m_contentviews.ListView
    _row_class = ListViewRow
    _required_elems = ['_root']


class TableView(containers.ContainerBase):
    """
    See: https://www.patternfly.org/patterns/table-view/
    """
    _model = m_contentviews.TableView

    # TODO
