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
import unittest

from tests.utility import xml_compare


class XmlCompareTests(unittest.TestCase):
    doc1 = '<doc><a>hello</a><b><c attr2="2" attr1="1">world</c></b></doc>'
    doc2 = '<doc><b><c attr1="1" attr2="2">world</c></b><a>hello</a></doc>'
    doc3 = '<doc><b><c>world</c></b><a>hello</a><d>not!</d></doc>'
    doc4 = '<doc><b><c attr1="1">world</c></b><a>hello</a></doc>'
    doc5 = '<doc><c attr1="1">world</c><a>hello</a></doc>'

    soap_doc1 = '''<?xml version="1.0" encoding="UTF-8"?>

      <soapenv:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
      xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">

      <soapenv:Body>
      <UpdateDateTime xmlns="urn:vim25">
          <_this type="HostDateTimeSystem">dateTimeSystem-14</_this>
          <dateTime>2014-08-19T04:29:36.070918-04:00</dateTime>
      </UpdateDateTime>
      </soapenv:Body>

      </soapenv:Envelope>'''

    soap_doc2 = '''<?xml version="1.0" encoding="UTF-8"?>

      <soapenv:Envelope
      xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">

      <soapenv:Body><UpdateDateTime xmlns="urn:vim25">
      <_this type="HostDateTimeSystem">dateTimeSystem-14</_this>
      <dateTime>2014-08-19T04:29:36.070918-04:00</dateTime>
      </UpdateDateTime>
      </soapenv:Body>

      </soapenv:Envelope>'''

    soap_doc3 = '''<?xml version="1.0" encoding="UTF-8"?>

      <soapenv:Envelope
      xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Body><UpdateDateTime xmlns="urn:vim25">
      <_this type="HostDateTimeSystem">dateTimeSystem-14</_this>
      <dateTime>2013-08-19T04:29:36.070918-04:00</dateTime></UpdateDateTime>
      </soapenv:Body>

      </soapenv:Envelope>'''

    def test_full_compare(self):
        self.assertTrue(xml_compare.full_compare(XmlCompareTests.doc1,
                                                 XmlCompareTests.doc2))
        self.assertFalse(xml_compare.full_compare(XmlCompareTests.doc1,
                                                  XmlCompareTests.doc3))
        self.assertFalse(xml_compare.full_compare(XmlCompareTests.doc1,
                                                  XmlCompareTests.doc4))

    def test_node_wise_compare(self):
        self.assertTrue(xml_compare.node_wise(XmlCompareTests.doc3,
                                              XmlCompareTests.doc4,
                                              'a'))
        self.assertFalse(xml_compare.node_wise(XmlCompareTests.doc3,
                                               XmlCompareTests.doc4,
                                               'b'))
        self.assertFalse(xml_compare.node_wise(XmlCompareTests.doc3,
                                               XmlCompareTests.doc4,
                                               'c'))
        self.assertFalse(xml_compare.node_wise(XmlCompareTests.doc4,
                                               XmlCompareTests.doc5,
                                               'b'))

    def test_soap_compare(self):
        self.assertTrue(xml_compare.soap_compare(XmlCompareTests.soap_doc1,
                                                 XmlCompareTests.soap_doc2))
        self.assertFalse(xml_compare.soap_compare(XmlCompareTests.soap_doc1,
                                                  XmlCompareTests.soap_doc3))

    def test_soap_node_compare(self):
        self.assertTrue(xml_compare.soap_node_wise(XmlCompareTests.soap_doc1,
                                                   XmlCompareTests.soap_doc2,
                                                   'soapenv:Body'))
        self.assertFalse(xml_compare.soap_node_wise(XmlCompareTests.soap_doc1,
                                                    XmlCompareTests.soap_doc3,
                                                    'soapenv:Body'))
