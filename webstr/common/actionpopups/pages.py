"""
Page objects for common dialogs.

Author: ltrilety
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
from webstr.common import timeouts
from webstr.common.actionpopups import models as m_actionpopups


class ActionPopupPanel(WebstrPage):
    """Base Action Pop Up Panel"""
    _model = m_actionpopups.ActionPopupPanelModel
    _timeout = timeouts.POPUP_WINDOW
    _reqired_elems = ['status_btn', 'stop_btn']

    def hit_stop_btn(self):
        """Hit stop button"""
        self._model.stop_btn.click()

    def hit_status_btn(self):
        """Hit status button"""
        self._model.status_btn.click()
