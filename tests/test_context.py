# VMware vSphere Python SDK
# Copyright (c) 2008-2017 VMware, Inc. All Rights Reserved.
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
from pyVim import context


class ContextTests(tests.VCRTestBase):
    @tests.VCRTestBase.my_vcr.use_cassette('test_context_connection.yaml',
                                           cassette_library_dir=tests.fixtures_path,
                                           record_mode='once')
    def test_context_connection(self):
        session_keys = []
        outer_si = connect.Connect(host='esxi00', pwd=tests.test_pwd,
                                   sslContext=tests.sslContext)
        for session in outer_si.content.sessionManager.sessionList:
            session_keys.append(session.key)

        print(session_keys)
        with context.Connection(host='esxi00', pwd=tests.test_pwd, sslContext=tests.sslContext) as si:
            key = si.content.sessionManager.currentSession.key
            print("Current session key is:\n\t", key, "\n")
            self.assertNotIn(key, session_keys)

        leftover_keys = []
        for session in outer_si.content.sessionManager.sessionList:
            key = session.key
            leftover_keys.append(key)
            self.assertIn(key, session_keys)

        print("Leftover keys:\n", leftover_keys)

    @tests.VCRTestBase.my_vcr.use_cassette('test_nested_context_connection.yaml',
                                           cassette_library_dir=tests.fixtures_path,
                                           record_mode='once')
    def test_nested_context_connection(self):
        session_keys = []
        conn = context.Connection(host='esxi00', pwd=tests.test_pwd, sslContext=tests.sslContext)
        outer_si = context.open(host='esxi00', pwd=tests.test_pwd, sslContext=tests.sslContext)
        for session in outer_si.content.sessionManager.sessionList:
            session_keys.append(session.key)

        print(session_keys)
        with conn as si:
            key = si.content.sessionManager.currentSession.key
            print("Current session key is:\n\t", key, "\n")
            self.assertNotIn(key, session_keys)
            with conn as inner_si:
                inner_key = inner_si.content.sessionManager.currentSession.key
                self.assertNotIn(inner_key, session_keys)
                print("Inner session key is:\n\t", inner_key, "\n")
                self.assertEqual(key, inner_key)
                with conn as inner_inner_si:
                    inner_inner_key = inner_inner_si.content.sessionManager.currentSession.key
                    self.assertNotIn(inner_inner_key, session_keys)
                    print("Inner inner session key is:\n\t", inner_key, "\n")
                    self.assertEqual(key, inner_inner_key)

            after_key = si.content.sessionManager.currentSession.key
            self.assertEqual(key, after_key)

        leftover_keys = []
        for session in outer_si.content.sessionManager.sessionList:
            key = session.key
            leftover_keys.append(key)
            self.assertIn(key, session_keys)

        print("Leftover keys:\n", leftover_keys)
