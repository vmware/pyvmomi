# VMware vSphere Python SDK
# Copyright (c) 2008-2015 VMware, Inc. All Rights Reserved.
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
from __future__ import absolute_import
# In VmomiSupport, to support dynamic type loading, all the data types are
# wrapped around using a meta type which can intercept attribute access and
# load the necessary nested classes. This can be implemented only in python 2.5
# version or more.
import sys
if sys.version_info < (2,5):
   sys.stderr.write("You need Python 2.5 or later to import pyVmomi module\n")
   sys.exit(1)

import pyVmomi.VmomiSupport
import pyVmomi._typeinfo_core
import pyVmomi._typeinfo_query
import pyVmomi._typeinfo_vim
import pyVmomi._typeinfo_pbm
import pyVmomi._typeinfo_sms
import pyVmomi._typeinfo_eam

# All data object types and fault types have DynamicData as an ancestor
# As well load it proactively.
# Note: This should be done before importing SoapAdapter as it uses
# some fault types
pyVmomi.VmomiSupport.GetVmodlType("vmodl.DynamicData")

from pyVmomi.SoapAdapter import SoapStubAdapter, StubAdapterBase, SoapCmdStubAdapter, \
    SessionOrientedStub, ThumbprintMismatchException

types = pyVmomi.VmomiSupport.types

# This will allow files to use Create** functions
# directly from pyVmomi
CreateEnumType = pyVmomi.VmomiSupport.CreateEnumType
CreateDataType = pyVmomi.VmomiSupport.CreateDataType
CreateManagedType = pyVmomi.VmomiSupport.CreateManagedType

# For all the top level names, creating a LazyModule object
# in the global namespace of pyVmomi. Files can just import the
# top level namespace and we will figure out what to load and when
# Examples:
# ALLOWED: from pyVmomi import vim
# NOT ALLOWED: from pyVmomi import vim.host
_globals = globals()
for name in pyVmomi.VmomiSupport._topLevelNames:
   upperCaseName = pyVmomi.VmomiSupport.Capitalize(name)
   obj = pyVmomi.VmomiSupport.LazyModule(name)
   _globals[name] = obj
   if pyVmomi.VmomiSupport._allowCapitalizedNames:
      _globals[upperCaseName] = obj
   if not hasattr(pyVmomi.VmomiSupport.types, name):
      setattr(pyVmomi.VmomiSupport.types, name, obj)
      if pyVmomi.VmomiSupport._allowCapitalizedNames:
         setattr(pyVmomi.VmomiSupport.types, upperCaseName, obj)
del _globals
