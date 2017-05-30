# VMware vSphere Python SDK
# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
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

import ssl
import unittest
import tests

from pyVmomi import pbm, VmomiSupport, SoapStubAdapter
from pyVim.connect import SmartConnectNoSSL


class PBMTests(tests.VCRTestBase):
    def get_pbm_connection(self, vpxd_stub):
        VmomiSupport.GetRequestContext()["vcSessionCookie"] = \
            vpxd_stub.cookie.split('"')[1]
        hostname = vpxd_stub.host.split(":")[0]
        pbm_stub = SoapStubAdapter(
            host=hostname,
            version="pbm.version.version11",
            path="/pbm/sdk",
            poolSize=0,
            sslContext=ssl._create_unverified_context())
        pbm_si = pbm.ServiceInstance("ServiceInstance", pbm_stub)
        pbm_content = pbm_si.RetrieveContent()
        return pbm_content

    def get_profile(self, profile_name, pbm_content):
        pm = pbm_content.profileManager
        profile_ids = pm.PbmQueryProfile(
            resourceType=pbm.profile.ResourceType(resourceType="STORAGE"),
            profileCategory="REQUIREMENT")
        if len(profile_ids) > 0:
            profiles = pm.PbmRetrieveContent(profileIds=profile_ids)
            for profile in profiles:
                if profile_name in profile.name:
                    return profile
        raise Exception('Profile not found')

    @tests.VCRTestBase.my_vcr.use_cassette('pbm_check_compatibility.yaml',
                                           cassette_library_dir=tests.fixtures_path,
                                           record_mode='Once')
    def test_pbm_check_compatibility(self):

        si = SmartConnectNoSSL(host='vcsa',
                               user='Administrator@vsphere.local',
                               pwd='Admin!23')

        # Connect to SPBM Endpoint
        pbm_content = self.get_pbm_connection(si._stub)

        sp = self.get_profile("test-profile", pbm_content)
        pbm_content.placementSolver.PbmCheckCompatibility(profile=sp.profileId)


if __name__ == '__main__':
    unittest.main()
