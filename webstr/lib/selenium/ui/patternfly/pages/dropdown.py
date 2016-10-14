"""
Page objects for patternfly dropdown menu:

https://www.patternfly.org/widgets/#dropdowns

Author: ltrilety
"""

from webstr.core import WebstrPage
from webstr.lib.selenium.ui.patternfly.models import dropdown as m_dropdown
import webstr.lib.selenium.ui.common.pages.containers as containers


class DropDownMenuRow(containers.ContainerRowBase):
    """
    Base class for drop down menu item.
    """
    _model = m_dropdown.DropDownMenuRow


class DropDownMenu(containers.ContainerBase):
    """
    Base page object for any active dropdown menu.
    """
    _model = m_dropdown.DropDownMenu
    _row_class = DropDownMenuRow
    _required_elems = ['_root']


class UpperDropDownMenu(DropDownMenu):
    """ Page object for dropdowns menu presented in upper menu """
    _model = m_dropdown.UpperDropDownMenu
