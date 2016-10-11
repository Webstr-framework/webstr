# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Page objects for patternfly Tabs

* https://www.patternfly.org/widgets/#tabs
"""

from raut.core import DynamicPageObject, PageObject
from raut.lib.selenium.ui.patternfly.models import tabs as m_tabs
import raut.lib.selenium.ui.common.pages.containers as containers


class Tab(containers.ContainerRowBase):
    """
    Item of Tabs.
    """
    _model = m_tabs.Tab
    _label = 'Tab'
    _required_elems = ['_root']

    @property
    def is_active(self):
        return self.get_attribute("class") == "active"



class Tabs(containers.ContainerBase):
    """
    See: https://www.patternfly.org/widgets/#tabs
    """
    _model = m_tabs.Tabs
    _row_class = Tab
    _required_elems = ['_root']
