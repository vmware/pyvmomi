# VMware vSphere Python SDK tests
#
# Copyright (c) 2008-2024 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
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
from datetime import datetime
from datetime import timedelta

import tests

from pyVim import connect
from pyVmomi.Iso8601 import TZManager
from pyVmomi import SoapAdapter

from vcr.stubs import VCRHTTPSConnection
from vcr import config


class Iso8601Tests(tests.VCRTestBase):

    @tests.VCRTestBase.my_vcr.use_cassette('test_vm_config_iso8601.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='once', decode_compressed_response=True)
    def test_vm_config_iso8601(self):
        si = connect.SmartConnect(host='vcsa',
                                  user='my_user',
                                  pwd='my_password')

        search_index = si.content.searchIndex
        uuid = "50201f05-b37c-db69-fda5-fb077e87af04"
        vm = search_index.FindByUuid(None, uuid, True, True)
        boot_time = vm.runtime.bootTime
        # NOTE (hartsock): assertIsNone does not work in Python 2.6
        self.assertTrue(boot_time is not None)

        # 2023-12-12T10:06:39Z
        expected_time = datetime(2023, 12, 12, 10, 6, 39, 0,
                                 boot_time.tzinfo)
        self.assertEqual(expected_time, boot_time)

    def test_iso8601_set_datetime(self):

        # NOTE (hartsock): This test is an example of how to register
        # a fixture based test to compare the XML document that pyVmomi
        # is transmitting. We needed to invent a set of tools to effectively
        # compare logical XML documents to each other. In this case we are
        # only interested in the 'soapenv:Body' tag and its children.

        now_string = "2014-08-19T04:29:36.070918-04:00"
        # NOTE (hartsock): the strptime formatter has a bug in python 2.x
        # http://bugs.python.org/issue6641 so we're building the date time
        # using the constructor arguments instead of parsing it.
        now = datetime(2014, 8, 19, 4, 29, 36, 70918,
                       TZManager.GetTZInfo(
                           tzname='EDT',
                           utcOffset=timedelta(hours=-4, minutes=0)))

        def has_tag(doc):
            if doc is None:
                return False
            return '<dateTime>' in doc.decode("utf-8")

        def correct_time_string(doc):
            return '<dateTime>{0}</dateTime>'.format(now_string) in doc.decode("utf-8")

        def check_date_time_value(r1, r2):
            for r in [r1, r2]:
                if has_tag(r.body):
                    if not correct_time_string(r.body):
                        return False
            return True

        my_vcr = config.VCR(
            custom_patches=(
                (SoapAdapter, 'HTTPSConnection', VCRHTTPSConnection),))
        my_vcr.register_matcher('document', check_date_time_value)

        # NOTE (hartsock): the `match_on` option is altered to use the
        # look at the XML body sent to the server
        with my_vcr.use_cassette('iso8601_set_datetime.yaml',
                                 cassette_library_dir=tests.fixtures_path,
                                 record_mode='once',
                                 match_on=['method', 'scheme', 'host', 'port',
                                           'path', 'query', 'document'], decode_compressed_response=True):
            
            si = connect.SmartConnect(host='vcsa',
                                      user='my_user',
                                      pwd='my_password')

            search_index = si.content.searchIndex
            uuid = "4220824e-c2eb-ed46-47db-8e5746f5bde4"

            vm = search_index.FindByUuid(None, uuid, True)
            date_time_system = vm.runtime.host.configManager.dateTimeSystem
            # NOTE (hartsock): sending the date time 'now' to host.
            date_time_system.UpdateDateTime(now)
