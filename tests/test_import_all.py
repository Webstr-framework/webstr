"""
Very basic check of python compatibility of webstr modules (the unit tests are
expected to by run with both python 2.7 and python3). We try to just import every
webstr module, which would fail on a syntax error if the module is not compatible.
"""

import importlib
import pkgutil

import pytest


def list_submodules(module_path, module_prefix):
    """
    For given module, return list of full module path names for all submodules recursively.
    """
    return [name for _, name, _ in  pkgutil.walk_packages(path=[module_path], prefix=module_prefix)]

# parametrize makes this case run for every submodule in webstr module
@pytest.mark.parametrize("module", list_submodules("webstr", "webstr."))
def test_import(module):
    """
    Just try to import given module.
    """
    importlib.import_module(module)
