"""
Page model for patternfly/bootstrap modal window.

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


from webstr.core import By
from webstr.core import PageElement
from webstr.core import WebstrModel
from webstr.core import RootPageElement


class ModalWindowModel(WebstrModel):
    """
    Base page model class for any modal window.
    """
    _root = RootPageElement(by=By.XPATH, locator="//div[@class='modal-dialog']")
    header= PageElement(by=By.XPATH, locator=".//div[contains(@class, 'modal-header')]")
    body = PageElement(by=By.XPATH, locator=".//div[contains(@class, 'modal-body')]")
    footer = PageElement(by=By.XPATH, locator=".//div[contains(@class, 'modal-footer')]")
    # we expect that the title is always there
    title = PageElement(by=By.XPATH, locator=".//*[contains(@class, 'modal-title')]")
    # there is always a close button (in the right side of the header)
    close_btn = PageElement(by=By.XPATH, locator=".//button[@class='close']")
    # if there are more buttons available in a footer or a body of a modal window
    # you need to define them all in a subclass
