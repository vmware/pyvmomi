# VMware vSphere Python SDK
# Copyright (c) 2008-2015 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import os
import socket
import unittest

import vcr
from vcr import config
from vcr.stubs import VCRHTTPSConnection

from pyVmomi import SoapAdapter


def tests_resource_path(local_path=''):
    this_file = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_file, local_path)

# Fully qualified path to the fixtures directory underneath this module
fixtures_path = tests_resource_path('fixtures')


def monkey_patch_vcrpy():
    # TODO (hartsock): This should be unnecessary. Remove after vcrpy updates.
    vcr.stubs.VCRHTTPSConnection.is_verified = True
    vcr.stubs.VCRFakeSocket = socket.socket

class VCRTestBase(unittest.TestCase):
    my_vcr = config.VCR(
        custom_patches=((SoapAdapter, '_HTTPSConnection', VCRHTTPSConnection),))

    def setUp(self):
        monkey_patch_vcrpy()
        logging.basicConfig()
        vcr_log = logging.getLogger('vcr')
        vcr_log.setLevel(logging.WARNING)
