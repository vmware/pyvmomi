# Copyright (c) 2005-2024 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

import sys
import importlib

version_info = (
    8,
    0,
    3,
    0,
    1,
)

version_info_str = ".".join(str(v) for v in version_info)

if sys.version_info < (2, 7, 9):
    sys.stderr.write("pyVmomi requires Python 2.7.9 or newer")
    sys.exit(1)

_initialized = False


# Deprecated
# Definition precedes pyVmomi modules imports to escape circular
# dependency error if modules import _assert_not_initialized()
def _assert_not_initialized():
    if _initialized:
        raise RuntimeError("pyVmomi is already initialized!")


# Deprecated
try:
    settings = importlib.import_module('.pyVmomiSettings', 'pyVmomi')
except ImportError:
    settings = None

# Deprecated
# set default settings
_allowGetSet = getattr(settings, 'allowGetSet', True)
_allowCapitalizedNames = \
    getattr(settings, 'allowCapitalizedNames', True)
_binaryIsBytearray = \
    getattr(settings, 'binaryIsBytearray', False)
_legacyThumbprintException = \
    getattr(settings, 'legacyThumbprintException', False)


from . import VmomiSupport  # noqa: E402
from . import Feature  # noqa: E402
from ._typeinfos import load_typeinfos  # noqa: E402
load_typeinfos()

# All data object types and fault types have DynamicData as an ancestor
# As well load it proactively.
# Note: This should be done before importing SoapAdapter as it uses
# some fault types
VmomiSupport.GetVmodlType("vmodl.DynamicData")

from .SoapAdapter import (  # noqa: E402,F401
    SessionOrientedStub, SoapStubAdapter, StubAdapterBase)
if _legacyThumbprintException:
    from .Security import ThumbprintMismatchException  # noqa: F401

types = VmomiSupport.types

# This will allow files to use Create** functions
# directly from pyVmomi
CreateEnumType = VmomiSupport.CreateEnumType
CreateDataType = VmomiSupport.CreateDataType
CreateManagedType = VmomiSupport.CreateManagedType

# For all the top level names, creating a LazyModule object
# in the global namespace of pyVmomi. Files can just import the
# top level namespace and we will figure out what to load and when
# Examples:
# ALLOWED: from pyVmomi import vim
# NOT ALLOWED: from pyVmomi import vim.host
_globals = globals()
for name in VmomiSupport._topLevelNames:
    upperCaseName = VmomiSupport.Capitalize(name)
    obj = VmomiSupport.LazyModule(name)
    _globals[name] = obj
    if _allowCapitalizedNames:
        _globals[upperCaseName] = obj
    if not hasattr(VmomiSupport.types, name):
        setattr(VmomiSupport.types, name, obj)
        if _allowCapitalizedNames:
            setattr(VmomiSupport.types, upperCaseName, obj)
del _globals

# Deprecated
def init():
    _assert_not_initialized()
    Feature._init()
    global _initialized
    _initialized = True
