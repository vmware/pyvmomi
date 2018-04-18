# VMware vSphere Python SDK
# Copyright (c) 2016 VMware, Inc. All Rights Reserved.
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

from pyVmomi import vim
from pyVmomi.SoapAdapter import SoapStubAdapter, SoapResponseDeserializer
import unittest

#TODO: Fix the test Post 6.7 release
# class DeserializerTests(unittest.TestCase):
#
#     def test_deserialize_unknown_managed_method(self):
#         with open('tests/files/unknown_method.xml', 'rb') as f:
#             data = f.read()
#         stub = SoapStubAdapter(version="vim.version.version6")
#         deserializer = SoapResponseDeserializer(stub)
#         result = vim.TaskHistoryCollector._GetMethodInfo("ReadNext").result
#         obj = deserializer.Deserialize(data, result)
#         print(obj)
#         with self.assertRaisesRegexp(Exception, "Managed method LeaseMapDiskRegion is not available"):
#             obj[-1].name()

