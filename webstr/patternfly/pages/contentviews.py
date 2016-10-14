"""
Page objects for patternfly Content Views:

* https://www.patternfly.org/list-view/
* https://www.patternfly.org/patterns/table-view/
"""

from webstr.core import DynamicWebstrPage, WebstrPage
from webstr.patternfly.models import contentviews as m_contentviews
import webstr.common.pages.containers as containers


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
