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
import atexit
from datetime import datetime

from tests import fixtures_path
import unittest
import vcr

from pyVim import connect

class Iso8601Tests(unittest.TestCase):

    @vcr.use_cassette('test_vm_config_iso8601.yaml',
                      cassette_library_dir=fixtures_path, record_mode='once')
    def test_vm_config_iso8601(self):
        si = connect.SmartConnect(host='vcsa',
                                  user='my_user',
                                  pwd='my_password')
        atexit.register(connect.Disconnect, si)

        search_index = si.content.searchIndex
        uuid = "5001ad1b-c78d-179e-ecd7-1cc0e1cf1b96"
        vm = search_index.FindByUuid(None, uuid, True, True)
        boot_time = vm.runtime.bootTime
        # NOTE (hartsock): assertIsNone does not work in Python 2.6
        self.assertTrue(boot_time is not None)

        # 2014-08-05T17:50:20.594958Z
        expected_time = datetime(2014, 8, 5, 17, 50, 20, 594958,
                                 boot_time.tzinfo)
        self.assertEqual(expected_time, boot_time)

    @vcr.use_cassette('iso8601_set_datetime.yaml',
                      cassette_library_dir=fixtures_path, record_mode='none')
    def test_iso8601_set_datetime(self):
        now = datetime.utcnow()
        si = connect.SmartConnect(host='vcsa',
                                  user='my_user',
                                  pwd='my_password')
        atexit.register(connect.Disconnect, si)

        search_index = si.content.searchIndex
        uuid = "4c4c4544-0043-4d10-8056-b1c04f4c5331"
        host = search_index.FindByUuid(None, uuid, False)
        date_time_system = host.configManager.dateTimeSystem

        # NOTE (hartsock): sending the date time 'now' to host.
        date_time_system.UpdateDateTime(now)
