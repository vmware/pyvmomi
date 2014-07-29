# VMware vSphere Python SDK
# Copyright (c) 2008-2014 VMware, Inc. All Rights Reserved.
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
from tests import fixtures_path
import unittest
import vcr

from pyVim import connect
from pyVmomi import SoapStubAdapter
from pyVmomi import vim

class DeserializerTests(unittest.TestCase):

    @vcr.use_cassette('test_unknown_fault.yaml',
                      cassette_library_dir=fixtures_path, record_mode='once')
    def test_unknown_fault(self):
        # see: http://python3porting.com/noconv.html
        si = connect.Connect(host='vcsa',
                             user='my_user',
                             pwd='my_password')
        content = si.RetrieveContent()
        lm = content.licenseManager
        # NOTE (hartsock): assertIsNotNone does not work in Python 2.6
        self.assertTrue(lm is not None)
        lam = lm.licenseAssignmentManager
        # NOTE (hartsock): assertIsNotNone does not work in Python 2.6
        self.assertTrue(lam is not None)
        # cassette is altered to raise a fault here:
        fault = None
        try:
            lam.QueryAssignedLicenses()
        except Exception as ex:
            # NOTE (hartsock): not using 'assertRaises' so we can inspect obj
            fault = ex
        # NOTE (hartsock): assertIsNotNone does not work in Python 2.6
        self.assertTrue(fault is not None) # only until 2.6 support is dropped.
        # Observe that the malformed XML was reported up the stack to the
        # user so that field reports will contain SOAP message information.
        self.assertTrue('<detail> '
                        '<UnknownLicenseProblemFaultFault '
                        'xsi:type="UnknownLicenseProblemFault"> '
                        '<reason>unknownReason</reason>'
                        '</UnknownLicenseProblemFaultFault> '
                        '</detail>' in str(fault))
