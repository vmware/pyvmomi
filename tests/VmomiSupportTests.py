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

import unittest
from pyVmomi import VmomiSupport

__author__ = 'Michael Rice <michael@michaelrice.org>'


class VmomiSupportTest(unittest.TestCase):
    """Unittests for the VmomiSupport class."""

    def setUp(self):
        self.wsdl_types = VmomiSupport.GetWsdlTypes()

    def test_get_wsdl_types_not_none(self):
        self.assertTrue(self.wsdl_types is not None)

    def test_capitalize(self):
        before = "the brown dog."
        after = "The brown dog."
        result = VmomiSupport.Capitalize(before)
        self.assertTrue(after == result)

    def test_uncapitalize(self):
        before = "The Brown fox."
        after = "the Brown fox."
        result = VmomiSupport.Uncapitalize(before)
        self.assertTrue(after == result)

    def test_get_version_namespace(self):
        version_namespace = 'vim.version.version7'
        version = VmomiSupport.GetVersionNamespace(version_namespace)
        self.assertEquals('vim25/5.0', version)

    def test_get_wsdl_namespace(self):
        version = 'vim.version.version7'
        self.assertEquals('urn:vim25', VmomiSupport.GetWsdlNamespace(version))


if __name__ == "__main__":
    unittest.main()
