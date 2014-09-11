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

import tests
import unittest
import vcr

from pyVim import connect
from pyVmomi import vim


class ConnectionTests(tests.VCRTestBase):

    @vcr.use_cassette('basic_connection.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_basic_connection(self):
        # see: http://python3porting.com/noconv.html
        si = connect.Connect(host='vcsa',
                             user='my_user',
                             pwd='my_password')
        cookie = si._stub.cookie
        session_id = si.content.sessionManager.currentSession.key
        # NOTE (hartsock): The cookie value should never change during
        # a connected session. That should be verifiable in these tests.
        self.assertEqual(cookie, si._stub.cookie)
        # NOTE (hartsock): assertIsNotNone does not work in Python 2.6
        self.assertTrue(session_id is not None)
        self.assertEqual('52773cd3-35c6-b40a-17f1-fe664a9f08f3', session_id)
        self.assertTrue(session_id in cookie)

    @vcr.use_cassette('basic_connection_bad_password.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_basic_connection_bad_password(self):
        def should_fail():
            connect.Connect(host='vcsa',
                            user='my_user',
                            pwd='bad_password')

        self.assertRaises(vim.fault.InvalidLogin, should_fail)

    @vcr.use_cassette('smart_connection.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_smart_connection(self):
        # see: http://python3porting.com/noconv.html
        si = connect.SmartConnect(host='vcsa',
                                  user='my_user',
                                  pwd='my_password')
        session_id = si.content.sessionManager.currentSession.key
        # NOTE (hartsock): assertIsNotNone does not work in Python 2.6
        self.assertTrue(session_id is not None)
        self.assertEqual('52773cd3-35c6-b40a-17f1-fe664a9f08f3', session_id)

    def test_disconnect_on_no_connection(self):
        connect.Disconnect(None)

    @vcr.use_cassette('ssl_tunnel.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_ssl_tunnel(self):
        connect.SoapStubAdapter('sdkTunnel', 8089, httpProxyHost='vcsa').GetConnection()

if __name__ == '__main__':
    unittest.main()