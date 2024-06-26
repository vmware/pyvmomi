# VMware vSphere Python SDK tests
#
# Copyright (c) 2017-2024 Broadcom. All Rights Reserved.
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

import tests

from pyVim import connect
from pyVmomi import vim


class SoapAdapterTests(tests.VCRTestBase):
    def test_invoke_method_login_session_exception(self):
        def login_fail(*args, **kwargs):
            raise vim_session.SESSION_EXCEPTIONS[0]()

        stub = connect.SoapStubAdapter()
        vim_session = connect.VimSessionOrientedStub(stub, login_fail)
        self.assertRaises(vim.fault.NotAuthenticated, vim_session.InvokeAccessor, "mo", "info")
