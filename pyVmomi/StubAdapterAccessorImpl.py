# VMware vSphere Python SDK
# Copyright (c) 2008-2022 VMware, Inc. All Rights Reserved.
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
from pyVmomi.VmomiSupport import GetVmodlType, ManagedObject, Object


class StubAdapterAccessorMixin:

   ## Retrieve a managed property
   #
   # @param self self
   # @param mo managed object
   # @param info property info
   def InvokeAccessor(self, mo, info):
      prop = info.name
      param = Object(name="prop", type=str, version=self.version, flags=0)
      info = Object(name=info.name,
                    type=ManagedObject,
                    wsdlName="Fetch",
                    version=info.version,
                    params=(param, ),
                    isTask=False,
                    resultFlags=info.flags,
                    result=info.type,
                    methodResult=info.type)
      return self.InvokeMethod(mo, info, (prop, ))
