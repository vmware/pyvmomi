# VMware vSphere Python SDK
# Copyright (c) 2008-2013 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# In VmomiSupport, to support dynamic type loading, all the data types are
# wrapped around using a meta type which can intercept attribute access and
# load the necessary nested classes. This can be implemented only in python 2.5
# version or more.
import sys

if sys.version_info < (2, 6):
    sys.stderr.write("You need Python 2.6 or later to import pyVmomi module\n")
    sys.exit(1)

import VmomiSupport
import CoreTypes

try:
    import ReflectTypes
except ImportError:
    pass
try:
    import ServerObjects
except ImportError:
    pass
try:
    import InternalServerObjects
except ImportError:
    pass

# Import all the known product-specific types
# XXX: Make this search the package for types?
try:
    import DrObjects
except ImportError:
    pass

try:
    import DrextObjects
except ImportError:
    pass

try:
    import HbrReplicaTypes
except ImportError:
    pass
try:
    import HmsObjects
except ImportError:
    pass
try:
    import HostdObjects
except ImportError:
    pass
try:
    import VpxObjects
except ImportError:
    pass
try:
    import VorbTypes
except ImportError:
    pass
try:
    import DodoTypes
except ImportError:
    pass
try:
    import VmwauthproxyTypes
except ImportError:
    pass
try:
    import DmsTypes
except ImportError:
    pass
try:
    import OmsTypes
except ImportError:
    pass
try:
    import HmoTypes
except ImportError:
    pass
try:
    import CimsfccTypes
except ImportError:
    pass
try:
    import TaskupdaterTypes
except ImportError:
    pass
try:
    import ImgFactTypes
except ImportError:
    pass

try:
    import VpxapiTypes
except ImportError:
    pass
try:
    import CsiObjects
except ImportError:
    pass

try:
    import HostdTypes
except ImportError:
    pass

try:
    import TaggingObjects
except ImportError:
    pass

try:
    import NfcTypes
except ImportError:
    pass

try:
    import SmsObjects
except ImportError:
    pass

try:
    import SpsObjects
except ImportError:
    pass

try:
    import DataserviceObjects
except ImportError:
    pass

# Start of update manager specific types
try:
    import IntegrityObjects
except ImportError:
    pass

try:
    import SysimageObjects
except ImportError:
    pass
# End of update manager specific types

try:
    import RbdTypes
except ImportError:
    pass

# Import Profile based management specific VMODL
try:
    import PbmObjects
except ImportError:
    pass

try:
    import CisLicenseTypes
except ImportError:
    pass

try:
    import TestTypes
except ImportError:
    pass

try:
    import SsoTypes
except ImportError:
    pass

try:
    import CisCmTypes
except ImportError:
    pass

try:
    import DataserviceTypes
except ImportError:
    pass


# All data object types and fault types have DynamicData as an ancestor
# As well load it proactively.
# Note: This should be done before importing SoapAdapter as it uses
# some fault types
VmomiSupport.GetVmodlType("vmodl.DynamicData")

from SoapAdapter import SoapStubAdapter, StubAdapterBase, SoapCmdStubAdapter, \
    SessionOrientedStub

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
    if VmomiSupport._allowCapitalizedNames:
        _globals[upperCaseName] = obj
    if not hasattr(VmomiSupport.types, name):
        setattr(VmomiSupport.types, name, obj)
        if VmomiSupport._allowCapitalizedNames:
            setattr(VmomiSupport.types, upperCaseName, obj)
del _globals
