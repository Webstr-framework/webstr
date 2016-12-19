"""
Page objects for patternfly Tabs

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


from webstr.core import DynamicWebstrPage, WebstrPage
from webstr.patternfly.models import tabs as m_tabs
import webstr.common.pages.containers as containers


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
