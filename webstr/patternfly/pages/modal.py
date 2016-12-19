"""
Page objects for patternfly/bootstrap modal window.

Modal window is a window which makes itself the only active element on the
page, so that one needs to close it first to access the rest of the page again.
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


from webstr.core import WebstrPage
from webstr.patternfly.models import modal as m_modal


class ModalWindow(WebstrPage):
    """
    Base page object class for any modal window.
    """
    _model = m_modal.ModalWindow
    _required_elems = ['header', 'body', 'footer', 'title', 'close_btn']

    def close(self):
        """
        Close the modal windown via default close button in the deader
        (a button labeled "X" in the top right corner).
        """
        self._model.close_btn.click()

    def get_title(self):
        return self._model.title.text
