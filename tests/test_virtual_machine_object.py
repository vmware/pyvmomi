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
                      record_mode='never')
    def test_vm_nic_data(self):
        data = {'ESXi-5.5-16': [],
                'ESXi-5.5-17': [],
                'ESXi-5.5-18': [],
                'ESXi11': ['00:0c:29:e1:e0:f8'],
                'ESXi12': ['00:50:56:b4:3c:3c'],
                'ESXi20': ['00:50:56:b4:fc:9b', '00:50:56:b4:28:e7'],
                'ESXi21': ['00:50:56:b4:8d:7a', '00:50:56:b4:39:b8'],
                'ESXi22': ['00:0c:29:36:b5:5a', '00:0c:29:36:b5:64'],
                'ESXi23': ['00:50:56:b4:91:f9', '00:50:56:b4:90:9f'],
                'ESXi38-v5.0': ['00:0c:29:ce:6a:d8', '00:0c:29:ce:6a:e2'],
                'MARVEL-Agents_of_Atlas': [],
                'MARVEL-Alex_Power': [],
                'MARVEL-Archangel': [],
                'MARVEL-Freak': [],
                'MARVEL-Hepzibah': [],
                'MARVEL-Mach_IV': [],
                'MARVEL-Serpent_Society': [],
                'MARVEL-Spectrum': [],
                'MARVEL-The_Hand': [],
                'MARVEL-Vanisher_(Ultimate)': [],
                'VCVA-5.5u1-11': ['00:0c:29:9d:a3:8c'],
                'VCVA-5.5u1-14': ['00:0c:29:75:21:2e'],
                'VCVA33': ['00:0c:29:e3:f9:f7'],
                'VCVA36': ['00:0c:29:44:8b:76'],
                'VCVA37-v5.0': ['00:50:56:b4:89:db'],
                'box': ['00:50:56:82:28:7d'],
                'box_copy': ['00:50:56:82:34:02'],
                'esx4.1.0': ['00:0c:29:1f:ec:ba', '00:0c:29:1f:ec:c4']}

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
