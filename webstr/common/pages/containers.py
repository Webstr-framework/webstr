"""

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


from webstr.core import WebstrPage, DynamicWebstrPage

import webstr.common.models.containers as m_containers



class ContainerIterator(object):
    """
    Iterator class for container.
    """

    def __init__(self, driver, row_element_list, row_class):
        """
        Arguments:
            driver: selenium web driver
            row_element_list: rows class attribute of container class
            row_class: class representing single line or item
        """
        self._driver = driver
        self._id_iter = self._get_instance_identifier_iterator(row_element_list)
        self._row_class = row_class

    def __iter__(self):
        """
        Following python iterator protocol.
        """
        return self

    def __next__(self):
        """
        Return current item element.
        """
        # this code expects that the table row doesn't disappear
        table_row = self._row_class(self._driver, next(self._id_iter))
        return table_row

    def _get_instance_identifier_iterator(self, row_element_list):
        """
        Return an iterator for all instance identifiers based on the current row element list.
        """
        if row_element_list is None:
            raise TypeError("container object is not iterable (rows are not initialized)")
        return iter(range(1, len(row_element_list) + 1))


class ContainerRowBase(DynamicWebstrPage):
    """
    A single item or line.
    """
    _model = m_containers.ContainerRowBase


class ContainerBase(WebstrPage):
    """
    Table shown under *Status* tab on the Task detail page.

    Class attributes:
        _model: related WebstrModel class
        _row_class: class representing single line or item
    """
    _model = m_containers.ContainerBase
    _row_class = ContainerRowBase
    _iter_class = ContainerIterator

    def __iter__(self):
        """
        Create new iterator object for this container.
        """
        row_element_list =  self._model.rows
        return self._iter_class(self.driver, row_element_list, row_class=self._row_class)

    def __len__(self):
        """
        Returns:
            number of rows
        """
        return len(self._model.rows)
