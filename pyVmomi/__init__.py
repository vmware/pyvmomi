# Copyright (c) 2005-2026 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

version_info = (
    9,
    1,
    1,
    0,
)

version_info_str = ".".join(str(v) for v in version_info)

from . import _init_utils  # noqa: E402
from . import VmomiSupport  # noqa: E402
from ._typeinfos import load_typeinfos  # noqa: E402
load_typeinfos()

# All data object types and fault types have DynamicData as an ancestor
# As well load it proactively.
# Note: This should be done before importing SoapAdapter as it uses
# some fault types
VmomiSupport.GetVmodlType("vmodl.DynamicData")

from .SoapAdapter import (  # noqa: E402,F401
    SessionOrientedStub, SoapStubAdapter, StubAdapterBase)

# Deprecated
# ThumbprintMismatchException was originally part of SoapAdapter and
# not in a separate Security module. The insertion into SoapAdapter
# and the top-level pyvmomi module was for backwards compatibility and
# is deprecated since pyVmomi 8.0.3
class ThumbprintMismatchExceptionIsNoMore:
    def __init__(self, *args, **kwargs):
        raise Exception("pyVmomi.ThumbprintMismatchException and"
                        " pyVmomi.SoapAdapter.ThumbprintMismatchException"
                        " are deprecated."
                        " Use pyVmomi.Security.ThumbprintMismatchException"
                        " instead.")

ThumbprintMismatchException = ThumbprintMismatchExceptionIsNoMore
setattr(SoapAdapter, 'ThumbprintMismatchException',
        ThumbprintMismatchExceptionIsNoMore)

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
    # TODO: remove when support for upper-case module names is dropped
    upperCaseName = VmomiSupport.Capitalize(name)
    obj = VmomiSupport.LazyModule(name)
    _globals[name] = obj
    if VmomiSupport._allowCapitalizedNames:
        _globals[upperCaseName] = obj
    if not hasattr(VmomiSupport.types, name):
        setattr(VmomiSupport.types, name, obj)
        if VmomiSupport._allowCapitalizedNames:
            setattr(VmomiSupport.types, upperCaseName, obj)
del _globals
