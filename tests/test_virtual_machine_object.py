# VMware vSphere Python SDK
# Copyright (c) 2008-2015 VMware, Inc. All Rights Reserved.
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
from __future__ import print_function

import tests

from pyVim import connect
from pyVmomi import vim


class VirtualMachineTests(tests.VCRTestBase):

    @tests.VCRTestBase.my_vcr.use_cassette('vm_nic_data.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='once', decode_compressed_response=True)
    def test_vm_nic_data(self):
        data = {
            'vCLS-fc35c4f3-c84c-4232-9446-e64ff2c9388c': [],
            'vCLS-8f66678f-3d69-4b58-a4c7-bae62203b573': [],
            'vCLS-32d7e67b-f3b4-485b-9685-b4b43c7f9c75': []
        }

        # see: http://python3porting.com/noconv.html
        si = connect.SmartConnect(host='vcsa',
                                  user='my_user',
                                  pwd='my_password')

        content = si.RetrieveContent()
        virtual_machines = content.viewManager.CreateContainerView(
            content.rootFolder, [vim.VirtualMachine], True)
        for virtual_machine in virtual_machines.view:
            name = virtual_machine.name
            self.assertTrue(name in data.keys())
            macs = data[name]
            if virtual_machine.guest:
                for net in virtual_machine.guest.net:
                    self.assertTrue(net.macAddress in macs)
