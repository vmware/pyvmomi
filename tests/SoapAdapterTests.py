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
from unittest import TestCase
from mock import Mock

import socket
import urllib
import urlparse
import httpretty

from tests import BaseTest
from tests import VIM_SERVICE_VERSIONS

from pyVim import connect
from pyVmomi import vim
from pyVmomi import vmodl
from pyVmomi import SoapAdapter

try:
   from xml.etree.ElementTree import ElementTree
except ImportError:
   from elementtree.ElementTree import ElementTree

class closing(object):
   """
   Helper class for using closable objects in a 'with' statement,
   similar to the one provided by contextlib.
   """
   def __init__(self, obj):
      self.obj = obj
   def __enter__(self):
      return self.obj
   def __exit__(self, *exc_info):
      self.obj.close()


LICENSE_QUERY_RESPONSE_BODY = (
'<?xml version=\'1.0\' encoding=\'UTF-8\'?>'
'<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" '
'xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" '
'xmlns:xsd="http://www.w3.org/2001/XMLSchema" '
'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
'<soapenv:Body>'
'<QueryLicenseEntriesResponse xmlns="urn:license">'
'<returnval>'
'<licenseId>1</licenseId>'
'<licenseKey>AAAAA-BBBBB-CCCCC-DDDDD-EEEEE</licenseKey>'
'<editionName>vCenter Server 5 Standard</editionName>'
'<costUnit>server</costUnit>'
'<costUnitNum>1</costUnitNum>'
'<capacity>64</capacity>'
'<expirationTimestamp>1420070400000</expirationTimestamp>'
'</returnval>'
'</QueryLicenseEntriesResponse>'
'</soapenv:Body>'
'</soapenv:Envelope>')


class SoapAdapterTests(TestCase):

    def test_malformed_exception(self):
        mocked_obj = Mock()
        mocked_obj.version = vim.version.version3
        deserializer = SoapAdapter.SoapResponseDeserializer(mocked_obj)

        tree = ElementTree()
        version_url = 'https://{0}:443/sdk/vimServiceVersions.xml'.format(
            self.host)
        httpretty.register_uri(httpretty.GET,
                               version_url,
                               body='<?xml version=\'1.0\' encoding=\'UTF-8\'?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><soapenv:Body><soapenv:Fault><faultcode>ServerFaultCode</faultcode><faultstring/><detail><LicenseUsageFaultFault xsi:type="LicenseUsageFault"><reason>dataTampered</reason></LicenseUsageFaultFault></detail></soapenv:Fault></soapenv:Body></soapenv:Envelope>',
                               code=200)
        with closing(urllib.urlopen(version_url)) as sock:
         if sock.getcode() == 200:
            tree.parse(sock)
            return tree
        obj = SoapAdapter.SoapResponseDeserializer(self).Deserialize(LICENSE_QUERY_RESPONSE_BODY, info.result)
        result = deserializer.Deserialize(LICENSE_QUERY_RESPONSE_BODY, )
        print result
