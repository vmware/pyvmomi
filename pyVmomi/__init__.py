# VMware vSphere Python SDK
# Copyright (c) 2008-2013 VMware, Inc. All Rights Reserved.
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

# In VmomiSupport, to support dynamic type loading, all the data types are
# wrapped around using a meta type which can intercept attribute access and
# load the necessary nested classes. This can be implemented only in python 2.5
# version or more.
from __future__ import absolute_import

import sys
if sys.version_info < (2,5):
   sys.stderr.write("You need Python 2.5 or later to import pyVmomi module\n")
   sys.exit(1)

import pyVmomi.VmomiSupport
import pyVmomi.CoreTypes

try:
   import ReflectTypes
except ImportError:
   pass

import pyVmomi.ServerObjects

try:
   import pyVmomi.InternalServerObjects
except ImportError:
   pass

# Import all the known product-specific types
# XXX: Make this search the package for types?
try:
   import pyVmomi.DrObjects
except ImportError:
   pass

try:
   import pyVmomi.DrextObjects
except ImportError:
   pass

try:
   import pyVmomi.HbrReplicaTypes
except ImportError:
   pass
try:
   import pyVmomi.HmsObjects
except ImportError:
   pass
try:
   import pyVmomi.HostdObjects
except ImportError:
   pass
try:
   import pyVmomi.VpxObjects
except ImportError:
   pass
try:
   import pyVmomi.VorbTypes
except ImportError:
   pass
try:
   import pyVmomi.DodoTypes
except ImportError:
   pass
try:
   import pyVmomi.VmwauthproxyTypes
except ImportError:
   pass
try:
   import pyVmomi.DmsTypes
except ImportError:
   pass
try:
   import pyVmomi.OmsTypes
except ImportError:
   pass
try:
   import pyVmomi.HmoTypes
except ImportError:
   pass
try:
   import pyVmomi.CimsfccTypes
except ImportError:
   pass
try:
   import pyVmomi.TaskupdaterTypes
except ImportError:
   pass
try:
   import pyVmomi.ImgFactTypes
except ImportError:
   pass

try:
   import pyVmomi.VpxapiTypes
except ImportError:
   pass
try:
   import pyVmomi.CsiObjects
except ImportError:
   pass

try:
   import pyVmomi.HostdTypes
except ImportError:
   pass

try:
   import pyVmomi.TaggingObjects
except ImportError:
   pass

try:
   import pyVmomi.NfcTypes
except ImportError:
   pass

try:
   import pyVmomi.SmsObjects
except ImportError:
   pass

try:
   import pyVmomi.SpsObjects
except ImportError:
   pass

try:
   import pyVmomi.DataserviceObjects
except ImportError:
   pass

# Start of update manager specific types
try:
   import pyVmomi.IntegrityObjects
except ImportError:
   pass

try:
   import pyVmomi.SysimageObjects
except ImportError:
   pass
# End of update manager specific types

try:
   import pyVmomi.RbdTypes
except ImportError:
   pass

# Import Profile based management specific VMODL
try:
   import pyVmomi.PbmObjects
except ImportError:
   pass

try:
   import pyVmomi.CisLicenseTypes
except ImportError:
   pass

try:
   import pyVmomi.TestTypes
except ImportError:
   pass

try:
   import pyVmomi.SsoTypes
except ImportError:
   pass

try:
   import pyVmomi.CisCmTypes
except ImportError:
    pass

try:
   import pyVmomi.DataserviceTypes
except ImportError:
   pass


# All data object types and fault types have DynamicData as an ancestor
# As well load it proactively.
# Note: This should be done before importing SoapAdapter as it uses
# some fault types
VmomiSupport.GetVmodlType("vmodl.DynamicData")

try:
    from SoapAdapter import SoapStubAdapter, StubAdapterBase, SoapCmdStubAdapter, \
        SessionOrientedStub
except ImportError:
    from pyVmomi.SoapAdapter import SoapStubAdapter, StubAdapterBase, SoapCmdStubAdapter, \
        SessionOrientedStub

types = VmomiSupport.types


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
