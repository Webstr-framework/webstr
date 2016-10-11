"""
Very basic check of python compatibility of webstr modules (the unit tests are
expected to by run with both python 2.7 and python3). We try to just import the
module, which would fail on a syntax error if the module is not compatible.
"""

import importlib
import pkgutil

import pytest


def list_submodules(module_path, module_prefix):
    """
    Return list of full module path names for all submodules of given module.
    """
    return [name for _, name, _ in  pkgutil.iter_modules(path=[module_path], prefix=module_prefix)]

@pytest.mark.parametrize("module", list_submodules("webstr/core", "webstr.core."))
def test_import_webstr_core(module):
    """
    Just try to import given module.
    """
    importlib.import_module(module)
