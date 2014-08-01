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
from tests import fixtures_path
import logging
from pprint import pprint
import unittest
import vcr

from pyVim import connect
from pyVmomi import vim


class ContainerViewTests(unittest.TestCase):

    def setUp(self):
        logging.basicConfig()
        vcr_log = logging.getLogger('vcr')
        vcr_log.setLevel(logging.DEBUG)

    @vcr.use_cassette('basic_container_view.yaml',
                      cassette_library_dir=fixtures_path, record_mode='once')
    def test_basic_container_view(self):
        # see: http://python3porting.com/noconv.html
        si = connect.SmartConnect(host='vcsa',
                                  user='my_user',
                                  pwd='my_password')
        atexit.register(connect.Disconnect, si)

        content = si.RetrieveContent()

        datacenter_object_view = content.viewManager.CreateContainerView(
            content.rootFolder, [vim.Datacenter], True)

        for datacenter in datacenter_object_view.view:
            datastores = datacenter.datastore
            # NOTE (hartsocks): the object handle here is a managed object
            # reference, until we ask for more details, no other detail is
            # transmitted. Our sample fixture is quite small.
            self.assertEqual(1, len(datastores))

        datacenter_object_view.Destroy()
