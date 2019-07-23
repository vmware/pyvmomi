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

import tests
import unittest
import sys

from pyVim import connect
from pyVmomi import vim

if sys.version_info >= (3, 3):
    from unittest.mock import patch, MagicMock
else:
    from mock import patch, MagicMock


class ConnectionTests(tests.VCRTestBase):

    @tests.VCRTestBase.my_vcr.use_cassette('basic_connection.yaml',
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
        self.assertEqual('52b5395a-85c2-9902-7835-13a9b77e1fec', session_id)

    @tests.VCRTestBase.my_vcr.use_cassette('sspi_connection.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_sspi_connection(self):
        # see: http://python3porting.com/noconv.html
        si = connect.Connect(host='vcsa',
                             mechanism='sspi',
                             b64token='my_base64token')
        cookie = si._stub.cookie
        session_id = si.content.sessionManager.currentSession.key
        # NOTE (hartsock): The cookie value should never change during
        # a connected session. That should be verifiable in these tests.
        self.assertEqual(cookie, si._stub.cookie)
        # NOTE (hartsock): assertIsNotNone does not work in Python 2.6
        self.assertTrue(session_id is not None)
        self.assertEqual('52b5395a-85c2-9902-7835-13a9b77e1fec', session_id)

    @tests.VCRTestBase.my_vcr.use_cassette('basic_connection_bad_password.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_basic_connection_bad_password(self):
        def should_fail():
            connect.Connect(host='vcsa',
                            user='my_user',
                            pwd='bad_password')

        self.assertRaises(vim.fault.InvalidLogin, should_fail)

    @tests.VCRTestBase.my_vcr.use_cassette('smart_connection.yaml',
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
        self.assertEqual('52ad453a-13a7-e8af-9186-a1b5c5ab85b7', session_id)

    def test_disconnect_on_no_connection(self):
        connect.Disconnect(None)

    @tests.VCRTestBase.my_vcr.use_cassette('ssl_tunnel.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_ssl_tunnel(self):
        connect.SoapStubAdapter('sdkTunnel', 8089, httpProxyHost='vcsa').GetConnection()

    def test_ssl_tunnel_http_failure(self):
        import socket
        def should_fail():
            conn = connect.SoapStubAdapter('vcsa', 80, httpProxyHost='unreachable').GetConnection()
            conn.request('GET', '/')
            conn.getresponse()
        self.assertRaises((OSError, socket.gaierror), should_fail)

    @tests.VCRTestBase.my_vcr.use_cassette('ssl_tunnel.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_http_proxy(self):
        connect.SoapStubAdapter('sdkTunnel', 8089, httpProxyHost='vcsa').GetConnection()

    @patch('six.moves.http_client.HTTPSConnection')
    def test_http_proxy_with_cert_file(self, hs):
        conn = connect.SoapStubAdapter(
            'sdkTunnel', 8089, httpProxyHost='vcsa',
            certKeyFile='my_key_file', certFile='my_cert_file').GetConnection()
        conn.request('GET', '/')
        hs.assert_called_once_with('vcsa:80', cert_file='my_cert_file', key_file='my_key_file')
        conn.set_tunnel.assert_called_once_with('sdkTunnel:8089')

    @tests.VCRTestBase.my_vcr.use_cassette('http_proxy.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='once')
    def test_http_proxy(self):
        conn = connect.SoapStubAdapter(
            'vcenter.test', httpProxyHost='my-http-proxy',
            httpProxyPort=8080).GetConnection()
        self.assertEqual(conn._tunnel_host, 'vcenter.test')
        self.assertEqual(conn._tunnel_port, 443)
        conn.request('GET', '/')
        conn.getresponse()


if __name__ == '__main__':
    unittest.main()
