# -*- coding: utf-8 -*-

# VMware vSphere Python SDK
# Copyright (c) 2008-2018 VMware, Inc. All Rights Reserved.
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

import tests

from pyVim import connect
from pyVmomi import vim
from pyVmomi.VmomiSupport import VmomiJSONEncoder, templateOf
from six import PY3

import atexit
import inspect
import json
import os


class JSONTests(tests.VCRTestBase):
    @property
    def datacenter(self):
        return getattr(vim, 'Datacenter')('datacenter-2', self.si._stub)
        
    @property
    def datastore(self):
        return getattr(vim, 'Datastore')('datastore-15', self.si._stub)
        
    @property
    def host(self):
        return getattr(vim, 'HostSystem')('host-14', self.si._stub)

    @property
    def network(self):
        return getattr(vim, 'Network')('network-16', self.si._stub)
        
    @property
    def si(self):
        if not hasattr(self, '_si'):
            self._si = connect.SmartConnectNoSSL(
                host='vcenter', user='my_user', pwd='my_pass')
            atexit.register(connect.Disconnect, self._si)
        return self._si

    @property
    def vm(self):
        return getattr(vim, 'VirtualMachine')('vm-127', self.si._stub)

    @property
    def vm2(self):
        return getattr(vim, 'VirtualMachine')('vm-22', self.si._stub)

    def expect(self, data):
        """
        Handle results expectation.  If the expect data file does not
        exist we write one out.  Otherwise we read and compare.  This
        means it is the responsibility of the individual creating the
        .expect files to ensure they are correct.
        """
        testname = inspect.stack()[1][3]
        expectfile = 'tests/files/{0}.expect'.format(testname)
        if os.path.exists(expectfile):
            with open(expectfile, 'r') as file:
                expectdata = file.read()
            self.assertEqual(data, expectdata)
        else:
            with open(expectfile, 'w') as file:
                file.write(data)

    # NOTE: sort_keys is needed for expect comparison to work;
    #                 not required for consumption

    # Explodes the VM
    # By definition if the input is a ManagedObject then it explodes.
    @tests.VCRTestBase.my_vcr.use_cassette(
        'test_json_vm_explode_default.yaml',
        cassette_library_dir=tests.fixtures_path, record_mode='once')
    def test_json_vm_explode_default(self):
        raw = json.dumps(self.vm, cls=VmomiJSONEncoder, sort_keys=True)
        self.expect(raw)
        # Basic saniy check
        data = json.loads(raw)
        self.assertEqual(data['_vimid'], 'vm-127')
        self.assertEqual(data['_vimref'], 'vim.VirtualMachine:vm-127')
        self.assertEqual(data['_vimtype'], 'vim.VirtualMachine')
        self.assertEqual(data['overallStatus'], 'green')
        self.assertEqual(len(data['network']), 1)
        self.assertEqual(len(data['guest']['disk']), 1)

    # Explodes the VM and the VM's networks
    # Here self.vm is redundant (see above) but not harmful.
    @tests.VCRTestBase.my_vcr.use_cassette(
        'test_json_vm_explode_objs.yaml',
        cassette_library_dir=tests.fixtures_path, record_mode='once')
    def test_json_vm_explode_objs_match(self):
        to_explode = [self.vm]
        for item in self.vm.network:
            to_explode.append(item)
        self.expect(json.dumps(self.vm, cls=VmomiJSONEncoder, sort_keys=True,
                               explode=to_explode))

    # Explodes by type: all VirtualMachine and all of its snapshots
    @tests.VCRTestBase.my_vcr.use_cassette(
        'test_json_vm_explode_type.yaml',
        cassette_library_dir=tests.fixtures_path, record_mode='once')
    def test_json_vm_explode_type_match(self):
        self.expect(json.dumps([self.vm, self.vm2], cls=VmomiJSONEncoder,
                               sort_keys=True,
                               explode=[templateOf('VirtualMachine'),
                                        templateOf('VirtualMachineSnapshot')]))

    # Test Datacenter
    @tests.VCRTestBase.my_vcr.use_cassette(
        'test_json_datacenter_explode.yaml',
        cassette_library_dir=tests.fixtures_path, record_mode='once')
    def test_json_datacenter_explode(self):
          self.expect(json.dumps(self.datacenter, cls=VmomiJSONEncoder,
                                 sort_keys=True))

    # Test Datastore
    @tests.VCRTestBase.my_vcr.use_cassette(
        'test_json_datastore_explode.yaml',
        cassette_library_dir=tests.fixtures_path, record_mode='once')
    def test_json_datastore_explode(self):
          self.expect(json.dumps(self.datastore, cls=VmomiJSONEncoder,
                                 sort_keys=True))

    # Test HostSystem
    @tests.VCRTestBase.my_vcr.use_cassette(
        'test_json_host_explode.yaml',
        cassette_library_dir=tests.fixtures_path, record_mode='once')
    def test_json_host_explode(self):
          self.expect(json.dumps(self.host, cls=VmomiJSONEncoder,
                                 sort_keys=True))

    # Test Network
    @tests.VCRTestBase.my_vcr.use_cassette(
        'test_json_network_explode.yaml',
        cassette_library_dir=tests.fixtures_path, record_mode='once')
    def test_json_network_explode(self):
          self.expect(json.dumps(self.network, cls=VmomiJSONEncoder,
                                 sort_keys=True))
