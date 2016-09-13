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


class ManagedObjectTests(tests.VCRTestBase):

    @tests.VCRTestBase.my_vcr.use_cassette('root_folder_parent.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='once')
    def test_root_folder_parent(self):
        # see: http://python3porting.com/noconv.html
        si = connect.SmartConnect(host='vcsa',
                                  user='my_user',
                                  pwd='my_password')

        root_folder = si.content.rootFolder
        self.assertTrue(hasattr(root_folder, 'parent'))
        # NOTE (hartsock): assertIsNone does not work in Python 2.6
        self.assertTrue(root_folder.parent is None)
