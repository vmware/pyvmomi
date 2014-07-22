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

"""Unittests for the SoapAdapter Class in pyVmomi
"""
__author__ = 'Michael Rice <michael@michaelrice.org>'

import unittest
from pyVmomi import SoapAdapter


class SoapAdapterTests(unittest.TestCase):

    def test_xml_escape(self):
        """Tests the XmlEscape function.

        This function should return &lt; for <
        &gt; for > and &amp; for &
        """
        before = "<tag>hello & world</tag>"
        after = "&lt;tag&gt;hello &amp; world&lt;/tag&gt;"
        result = SoapAdapter.XmlEscape(before)
        self.assertEquals(after, result)

    def test_serialize_fault_detail_type_error(self):
        """Tests to verify a TypeError is rasied if the fault is
        not a MethodFault.
        """
        fault = "This is not a valid MethodFault"
        self.assertRaises(TypeError, SoapAdapter.SerializeFaultDetail, fault)


if __name__ == '__main__':
    unittest.main()