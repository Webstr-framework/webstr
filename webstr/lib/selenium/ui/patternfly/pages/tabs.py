"""
Page objects for patternfly Tabs

* https://www.patternfly.org/widgets/#tabs
"""

from webstr.core import DynamicPageObject, PageObject
from webstr.lib.selenium.ui.patternfly.models import tabs as m_tabs
import webstr.lib.selenium.ui.common.pages.containers as containers


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
