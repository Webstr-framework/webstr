"""
"""

from webstr.core import WebstrModel, DynamicWebstrModel, By


class ContainerBase(WebstrModel):
    """
    Base class for any container like model, such as list, table, ...

    Class attributes:
        rows: list of all elements (should be defined in a subclass)
    """
    rows = None


class ContainerRowBase(DynamicWebstrModel):
    """
    Base class for a row in a container, such as item in a list, or a line in a table, ...
    """
