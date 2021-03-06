"""
Page objects for patternfly Content Views:

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


from webstr.core import DynamicWebstrPage, WebstrPage
from webstr.patternfly.contentviews import models as m_contentviews
import webstr.common.containers.pages as containers


class ListViewRow(containers.ContainerRowBase):
    """
    Item of a List View.
    """
    _model = m_contentviews.ListViewRowModel
    _label = 'ListView row'
    _required_elems = ['_root']


class ListView(containers.ContainerBase):
    """
    See: https://www.patternfly.org/list-view/
    """
    _model = m_contentviews.ListViewModel
    _row_class = ListViewRow
    _required_elems = ['_root']


class TableViewRow(containers.ContainerRowBase):
    """
    Item of a Table View.
    """
    _model = m_contentviews.TableViewRowModel
    _label = 'TableView row'
    _required_elems = ['_root']


class TableView(containers.ContainerBase):
    """
    See: https://www.patternfly.org/patterns/table-view/
    """
    _model = m_contentviews.TableViewModel
    _row_class = TableViewRow
    _required_elems = ['_root']
