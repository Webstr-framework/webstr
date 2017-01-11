"""
Very basic check of python compatibility of webstr modules (the unit tests are
expected to by run with both python 2.7 and python3). We try to just import every
webstr module, which would fail on a syntax error if the module is not compatible.
"""

import importlib
import inspect
import pkgutil
import sys

import pytest

import webstr.core.model


def list_submodules(module_path, module_prefix):
    """
    For given module, return list of full module path names for all submodules recursively.
    """
    return [name for _, name, _ in  pkgutil.walk_packages(path=[module_path], prefix=module_prefix)]


def list_model_submodules(module_path, module_prefix):
    """
    For given module, return list of full module path names for all model submodules recursively.
    """
    return [name for name in list_submodules(module_path, module_prefix) if name.endswith("models")]


# parametrize makes this case run for every submodule in webstr module
@pytest.mark.parametrize("module", list_submodules("webstr", "webstr."))
def test_import(module):
    """
    Just try to import given module.
    """
    importlib.import_module(module)


@pytest.mark.parametrize("module", list_model_submodules("webstr", "webstr."))
def test_models_module_naming_scheme(module):
    """
    Check that all names of all classess from models modules ends with 'Model' suffix.
    """
    importlib.import_module(module)
    # list of classess from given module
    class_list = inspect.getmembers(sys.modules[module], inspect.isclass)
    for class_name, class_type in class_list:
        # filter out classess which are there because of some __init__.py hack
        # eg. 'By' class could be there and needs to be ignored
        class_module = str(class_type.__module__)
        if class_module != module:
            continue
        # moreover filter out Element classess (those can be present in model module)
        if issubclass(class_type, webstr.core.model.BasePageElement) or \
           issubclass(class_type, webstr.core.model.BaseWebElementHelper):
            continue
        # actuall check: model class name should end with "Model" suffix
        assert class_name.endswith("Model")
