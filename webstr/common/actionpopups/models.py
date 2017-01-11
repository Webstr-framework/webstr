"""
Page models for common action popup panels.

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


from webstr.core import WebstrModel, RootPageElement, By
from webstr.common.form import models


class ActionPopupPanelModel(WebstrModel):
    """ Base Action Pop Up Panel model """
    _root = RootPageElement(By.CLASS_NAME, "actionPanelPopupPanel")

    status_btn = models.Button(By.XPATH, '//div[@class="actionPanelPopupPanel"]//td[contains(text(), "Status")]')
    stop_btn = models.Button(By.XPATH, '//div[@class="actionPanelPopupPanel"]//td[contains(text(), "Stop")]')
