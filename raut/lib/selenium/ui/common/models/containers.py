# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
"""

from raut.core import PageModel, DynamicPageModel, By


class ContainerBase(PageModel):
  """
  Base class for any container like model, such as list, table, ...

  Class attributes:
      rows: list of all elements (should be defined in a subclass)
  """
  rows = None


class ContainerRowBase(DynamicPageModel):
  """
  Base class for a row in a container, such as item in a list, or a line in a table, ...
  """
