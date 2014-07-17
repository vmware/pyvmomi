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

from unittest import TestCase
from mock import Mock

import requests
import httpretty

from pyVmomi import vim
from pyVmomi import vmodl
from pyVmomi import SoapAdapter

# 'https://test.com:443//sdk/vimServiceVersions.xml'
VIM_SERVICE_VERSIONS = """<!--

   Copyright 2008-2012 VMware, Inc.  All rights reserved.
-->
<namespaces version="1.0">
<namespace>
<name>urn:vim25</name>
<version>5.5</version>
<priorVersions>
<version>5.1</version>
<version>5.0</version>
<version>4.1</version>
<version>4.0</version>
<version>2.5u2</version>
<version>2.5</version>
</priorVersions>
</namespace>
<namespace>
<name>urn:vim2</name>
<version>2.0</version>
</namespace>
</namespaces>"""

class BaseTest(TestCase):

    @property
    def host(self):
        return self.test_host

    def setUp(self):
        self.test_host = '172.16.16.131'
        httpretty.enable()
        version_url = 'https://{0}//sdk/vimServiceVersions.xml'.format(
            self.host)
        httpretty.register_uri(httpretty.GET,
                               version_url,
                               body=VIM_SERVICE_VERSIONS,
                               code=200)

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()