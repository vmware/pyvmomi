"""
A python helper module to do SSO related operations.
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2012, 2017 VMware, Inc. All rights reserved.'

#Standard library imports.
import six.moves.http_client
import re
from six import PY3
if PY3:
    from html import escape
else:
    from cgi import escape
import sys
import datetime
import base64
import hashlib

from pyVmomi import ThumbprintMismatchException

from uuid import uuid4
from io import BytesIO
from six.moves.urllib.parse import urlparse
#Third-party imports.
from lxml import etree
from OpenSSL import crypto
import ssl

UTF_8 = 'utf-8'
SHA256 = 'sha256'
SHA512 = 'sha512'

def _extract_certificate(cert):
    '''
    Extract DER certificate/private key from DER/base64-ed DER/PEM string.

    @type           cert: C{str}
    @param          cert: Certificate/private key in one of three supported formats.

    @rtype: C{str}
    @return: Certificate/private key in DER (binary ASN.1) format.
    '''
    if not cert:
        raise IOError('Empty certificate')
    signature = cert[0]
    # DER certificate is sequence.  ASN.1 sequence is 0x30.
    if signature == '\x30':
        return cert
    # PEM without preamble.  Base64-encoded 0x30 is 0x4D.
    if signature == '\x4D':
        return base64.b64decode(cert)
    # PEM with preamble.  Starts with '-'.
    if signature == '-':
        return base64.b64decode(re.sub('-----[A-Z ]*-----', '', cert))
    # Unknown format.
    raise IOError('Invalid certificate file format')

#time.strftime() method returns 6 digit millisecond
#Formatting time with 3 digit milliseconds
def format_time(time):
    return time[:-3] + 'Z'

class SoapException(Exception):
    '''
    Exception raised in case of STS request failure.
    '''
    def __init__(self, soap_msg, fault_code, fault_string):
        '''
        Initializer for SoapException.

        @type      soap_msg: C{str}
        @param     soap_msg: the soap fault XML returned by STS
        @type    fault_code: C{str}
        @param   fault_code: The fault code returned by STS.
        @type  fault_string: C{str}
        @param fault_string: The fault string returned by STS.
        '''
        self._soap_msg = soap_msg
        self._fault_code = fault_code
        self._fault_string = fault_string
        Exception.__init__(self)

    def __str__(self):
        '''
        Returns the string representation of SoapException.

        @rtype: C{str}
        @return: string representation of SoapException
        '''
        return ("SoapException:\nfaultcode: %(_fault_code)s\n"
                "faultstring: %(_fault_string)s\n"
                "faultxml: %(_soap_msg)s" % self.__dict__)


class SSOHTTPSConnection(six.moves.http_client.HTTPSConnection):
    '''
    An HTTPS class that verifies server's certificate on connect.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initializer.  See httplib.HTTPSConnection for other arguments
        than thumbprint and server_cert.

        At least one of thumbprint, server_cert should be provided,
        otherwise server certificate is not validated.

        @type           thumbprint: C(str)
        @param          thumbprint: Expected SHA-1 thumbprint of the server
                                    certificate.  May be None.

        @type          server_cert: C(str)
        @param         server_cert: File with expected server certificate.
                                    May be None.
        '''
        self.server_thumbprint = kwargs.pop('thumbprint')
        if self.server_thumbprint is not None:
            self.server_thumbprint = re.sub(':', '',
                                            self.server_thumbprint.lower())
        server_cert_path = kwargs.pop('server_cert')
        if server_cert_path is not None:
            with open(server_cert_path, 'rb') as f:
                server_cert = f.read().decode(UTF_8)
            self.server_cert = _extract_certificate(server_cert)
        else:
            self.server_cert = None
        six.moves.http_client.HTTPSConnection.__init__(self, *args, **kwargs)

    def _check_cert(self, peerCert):
        '''
        Verify that peer certificate matches one we expect.

        @type             peerCert: C(str)
        @param            peerCert: Server certificate in DER format.

        @rtype: boolean
        @return: True if peerCert is acceptable.  False otherwise.
        '''
        if self.server_cert is not None:
            if peerCert != self.server_cert:
                self.sock.close()
                self.sock = None
                raise IOError("Invalid certificate")
        if self.server_thumbprint is not None:
            thumbprint = hashlib.sha1(peerCert).hexdigest().lower()  # pylint: disable=E1101
            if thumbprint != self.server_thumbprint:
                self.sock.close()
                self.sock = None
                raise ThumbprintMismatchException(
                   expected=self.server_thumbprint, actual=thumbprint)

    def connect(self):
        '''
        Connect method: connects to the remote system, and upon
        successful connection validates certificate.

        Throws an exception when something is wrong.  See
        httplib.HTTPSConnection.connect() for details.
        '''
        six.moves.http_client.HTTPSConnection.connect(self)

        self._check_cert(self.sock.getpeercert(True))


class SsoAuthenticator(object):
    '''
    A class to handle the transport layer communication between the client and
    the STS service.
    '''

    def __init__(self,
                 sts_url,
                 sts_cert=None,
                 thumbprint=None
                 ):
        '''
        Initializer for SsoAuthenticator.

        @type           sts_url: C{str}
        @param          sts_url: URL for the Security Token Service. Usually
                                 obtained by querying Component Manager.
        @type          sts_cert: C{str}
        @param         sts_cert: The file with public key of the Security
                                 Token Service.  Usually obtained from
                                 Component Manager and written to the file.
        @type        thumbprint: C{str}
        @param       thumbprint: The SHA-1 thumbprint of the certificate used
                                 by the Security Token Service.  It is same
                                 thumbprint you can pass to pyVmomi SoapAdapter.
        '''
        self._sts_cert = sts_cert
        self._sts_url = sts_url
        self._sts_thumbprint = thumbprint

    def perform_request(self,
                        soap_message,
                        public_key=None,
                        private_key=None,
                        ssl_context=None):
        '''
        Performs a Holder-of-Key SAML token request using the service user's
        certificates or a bearer token request using the user credentials.

        @type      soap_message: C{str}
        @param     soap_message: Authentication SOAP request.
        @type        public_key: C{str}
        @param       public_key: File containing the public key for the service
                                 user registered with SSO, in PEM format.
        @type       private_key: C{str}
        @param      private_key: File containing the private key for the service
                                 user registered with SSO, in PEM format.
        @type       ssl_context: C{ssl.SSLContext}
        @param      ssl_context: SSL context describing the various SSL options.
                                 It is only supported in Python 2.7.9 or higher.
        @rtype: C{str}
        @return: Response received from the STS after the HoK request.
        '''
        parsed = urlparse(self._sts_url)
        host = parsed.netloc  # pylint: disable=E1101
        encoded_message = soap_message.encode(UTF_8)
        if hasattr(ssl, '_create_unverified_context'):
            # Python 2.7.9 has stronger SSL certificate validation, so we need
            # to pass in a context when dealing with self-signed certificates.
            webservice = SSOHTTPSConnection(host=host,
                                            key_file=private_key,
                                            cert_file=public_key,
                                            server_cert=self._sts_cert,
                                            thumbprint=self._sts_thumbprint,
                                            context=ssl_context)
        else:
            # Versions of Python before 2.7.9 don't support
            # the context parameter, so don't pass it on.
            webservice = SSOHTTPSConnection(host=host,
                                            key_file=private_key,
                                            cert_file=public_key,
                                            server_cert=self._sts_cert,
                                            thumbprint=self._sts_thumbprint)

        webservice.putrequest("POST", parsed.path, skip_host=True)  # pylint: disable=E1101
        webservice.putheader("Host", host)
        webservice.putheader("User-Agent", "VMware/pyVmomi")
        webservice.putheader("Accept", "text/xml, multipart/related")
        webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
        webservice.putheader("Content-length", "%d" % len(encoded_message))
        webservice.putheader("Connection", "keep-alive")
        webservice.putheader("SOAPAction",
            "http://docs.oasis-open.org/ws-sx/ws-trust/200512/RST/Issue")
        webservice.endheaders()
        webservice.send(encoded_message)

        saml_response = webservice.getresponse()
        if saml_response.status != 200:
            faultraw = saml_response.read()
            # Hopefully it is utf-8 or us-ascii, not Apache error message in Shift-JIS.
            fault = faultraw.decode(UTF_8)
            # Best effort at figuring out a SOAP fault.
            if saml_response.status == 500 and fault and 'faultcode' in fault:
                fault_xml = etree.fromstring(faultraw)
                parsed_fault = fault_xml.xpath("//text()")
                if len(parsed_fault) == 2:
                    raise SoapException(fault, *parsed_fault)
            raise Exception("Got response %s: %s\n%s" %
                            (saml_response.status, saml_response.msg, fault))
        return saml_response.read()

    def get_bearer_saml_assertion(self,
                                  username,
                                  password,
                                  public_key=None,
                                  private_key=None,
                                  request_duration=60,
                                  token_duration=600,
                                  delegatable=False,
                                  renewable=False,
                                  ssl_context=None):
        '''
        Extracts the assertion from the Bearer Token received from the Security
        Token Service.

        @type          username: C{str}
        @param         username: Username for the user for which bearer token
                                 needs to be requested.
        @type          password: C{str}
        @param         password: Password for the user for which bearer token
                                 needs to be requested.
        @type        public_key: C{str}
        @param       public_key: File containing the public key for the service
                                 user registered with SSO, in PEM format.
        @type       private_key: C{str}
        @param      private_key: File containing the private key for the service
                                 user registered with SSO, in PEM format.

        @type  request_duration: C{long}
        @param request_duration: The duration for which the request is valid. If
                                 the STS receives this request after this
                                 duration, it is assumed to have expired. The
                                 duration is in seconds and the default is 60s.
        @type    token_duration: C{long}
        @param   token_duration: The duration for which the SAML token is issued
                                 for. The duration is specified in seconds and
                                 the default is 600s.
        @type       delegatable: C{boolean}
        @param      delegatable: Whether the generated token is delegatable or not
                                 The default value is False
        @type       ssl_context: C{ssl.SSLContext}
        @param      ssl_context: SSL context describing the various SSL options.
                                 It is only supported in Python 2.7.9 or higher.
        @rtype: C{str}
        @return: The SAML assertion in Unicode.
        '''
        request = SecurityTokenRequest(username=username,
                                       password=password,
                                       public_key=public_key,
                                       private_key=private_key,
                                       request_duration=request_duration,
                                       token_duration=token_duration)
        soap_message = request.construct_bearer_token_request(
            delegatable=delegatable, renewable=renewable)
        bearer_token = self.perform_request(soap_message,
                                            public_key,
                                            private_key,
                                            ssl_context)
        return etree.tostring(
                    _extract_element(etree.fromstring(bearer_token),
                        'Assertion',
                        {'saml2': "urn:oasis:names:tc:SAML:2.0:assertion"}),
                        pretty_print=False).decode(UTF_8)

    def _get_gss_soap_response(self,
                               binary_token,
                               request_duration=60,
                               token_duration=600,
                               delegatable=False,
                               renewable=False,
                               ssl_context=None):
        '''
        Extracts the assertion from the Bearer Token received from the Security
        Token Service using the binary token generated using either sspi or gss module.

        @type  binary_token: C{str}
        @param binary_token: The security token in base64 encoded format

        @type  request_duration: C{long}
        @param request_duration: The duration for which the request is valid. If
                                 the STS receives this request after this
                                 duration, it is assumed to have expired. The
                                 duration is in seconds and the default is 60s.
        @type    token_duration: C{long}
        @param   token_duration: The duration for which the SAML token is issued
                                 for. The duration is specified in seconds and
                                 the default is 600s.
        @type       delegatable: C{boolean}
        @param      delegatable: Whether the generated token is delegatable or not
                                 The default value is False
        @type         renewable: C{boolean}
        @param        renewable: Whether the generated token is renewable or not
                                 The default value is False
        @type       ssl_context: C{ssl.SSLContext}
        @param      ssl_context: SSL context describing the various SSL options.
                                 It is only supported in Python 2.7.9 or higher.
        @rtype: C{str}
        @return: The SAML assertion.
        '''
        request = SecurityTokenRequest(request_duration=request_duration,
                                       token_duration=token_duration,
                                       gss_binary_token=binary_token)
        soap_message = request.construct_bearer_token_request_with_binary_token(
            delegatable=delegatable, renewable=renewable)
        return self.perform_request(soap_message,
                                    ssl_context=ssl_context)

    def _get_bearer_saml_assertion_win(self,
                                       request_duration=60,
                                       token_duration=600,
                                       delegatable=False,
                                       renewable=False,
                                       ssl_context=None):
        '''
        Extracts the assertion from the Bearer Token received from the Security
        Token Service using the SSPI module.

        @type  request_duration: C{long}
        @param request_duration: The duration for which the request is valid. If
                                 the STS receives this request after this
                                 duration, it is assumed to have expired. The
                                 duration is in seconds and the default is 60s.
        @type    token_duration: C{long}
        @param   token_duration: The duration for which the SAML token is issued
                                 for. The duration is specified in seconds and
                                 the default is 600s.
        @type       delegatable: C{boolean}
        @param      delegatable: Whether the generated token is delegatable or not
                                 The default value is False
        @type         renewable: C{boolean}
        @param        renewable: Whether the generated token is renewable or not
                                 The default value is False
        @type       ssl_context: C{ssl.SSLContext}
        @param      ssl_context: SSL context describing the various SSL options.
                                 It is only supported in Python 2.7.9 or higher.
        @rtype: C{str}
        @return: The SAML assertion.
        '''
        import sspi, win32api
        spn = "sts/%s.com" % win32api.GetDomainName()
        sspiclient = sspi.ClientAuth("Kerberos", targetspn=spn)
        in_buf = None
        err = True
        # The following will keep running unless we receive a saml token or an error
        while True:
            err, out_buf = sspiclient.authorize(in_buf)
            sectoken = base64.b64encode(out_buf[0].Buffer)
            soap_response = self._get_gss_soap_response(sectoken,
                                request_duration, token_duration,
                                delegatable, renewable, ssl_context)
            et = etree.fromstring(soap_response)
            try:
                # Check if we have received a challenge token from the server
                element = _extract_element(et,
                        'BinaryExchange',
                        {'ns': "http://docs.oasis-open.org/ws-sx/ws-trust/200512"})
                negotiate_token = element.text
                out_buf[0].Buffer = base64.b64decode(negotiate_token)
                in_buf = out_buf
            except KeyError:
                # Response does not contain the negotiate token.
                # It should contain SAML token then.
                saml_token = etree.tostring(
                    _extract_element(
                        et,
                        'Assertion',
                        {'saml2': "urn:oasis:names:tc:SAML:2.0:assertion"}),
                    pretty_print=False).decode(UTF_8)
                break
        return saml_token

    def _get_bearer_saml_assertion_lin(self,
                                       request_duration=60,
                                       token_duration=600,
                                       delegatable=False,
                                       renewable=False):
        '''
        Extracts the assertion from the Bearer Token received from the Security
        Token Service using kerberos.

        @type  request_duration: C{long}
        @param request_duration: The duration for which the request is valid. If
                                 the STS receives this request after this
                                 duration, it is assumed to have expired. The
                                 duration is in seconds and the default is 60s.
        @type    token_duration: C{long}
        @param   token_duration: The duration for which the SAML token is issued
                                 for. The duration is specified in seconds and
                                 the default is 600s.
        @type       delegatable: C{boolean}
        @param      delegatable: Whether the generated token is delegatable or not
                                 The default value is False
        @type         renewable: C{boolean}
        @param        renewable: Whether the generated token is renewable or not
                                 The default value is False
        @rtype: C{str}
        @return: The SAML assertion in Unicode.
        '''
        import kerberos, platform
        service = 'host@%s' % platform.node()
        _, context = kerberos.authGSSClientInit(service, 0)
        challenge = ''
        # The following will keep running unless we receive a saml token or an error
        while True:
            # Call GSS step
            result = kerberos.authGSSClientStep(context, challenge)
            if result < 0:
                break
            sectoken = kerberos.authGSSClientResponse(context)
            soap_response = self._get_gss_soap_response(sectoken,
                                request_duration, token_duration, delegatable,
                                renewable)
            et = etree.fromstring(soap_response)
            try:
                # Check if we have received a challenge token from the server
                element = _extract_element(et,
                        'BinaryExchange',
                        {'ns': "http://docs.oasis-open.org/ws-sx/ws-trust/200512"})
                negotiate_token = element.text
                challenge = negotiate_token
            except KeyError:
                # Response does not contain the negotiate token.
                # It should contain SAML token then.
                saml_token = etree.tostring(
                    _extract_element(
                        et,
                        'Assertion',
                        {'saml2': "urn:oasis:names:tc:SAML:2.0:assertion"}),
                    pretty_print=False).decode(UTF_8)
                break
        return saml_token

    def get_bearer_saml_assertion_gss_api(self,
                                          request_duration=60,
                                          token_duration=600,
                                          delegatable=False,
                                          renewable=False):
        '''
        Extracts the assertion from the Bearer Token received from the Security
        Token Service using the GSS API.

        @type  request_duration: C{long}
        @param request_duration: The duration for which the request is valid. If
                                 the STS receives this request after this
                                 duration, it is assumed to have expired. The
                                 duration is in seconds and the default is 60s.
        @type    token_duration: C{long}
        @param   token_duration: The duration for which the SAML token is issued
                                 for. The duration is specified in seconds and
                                 the default is 600s.
        @type       delegatable: C{boolean}
        @param      delegatable: Whether the generated token is delegatable or not
                                 The default value is False
        @type         renewable: C{boolean}
        @param        renewable: Whether the generated token is renewable or not
                                 The default value is False
        @rtype: C{str}
        @return: The SAML assertion.
        '''
        if sys.platform == "win32":
            saml_token = self._get_bearer_saml_assertion_win(request_duration,
                            token_duration, delegatable, renewable)
        else:
            raise Exception("Currently, not supported on this platform")
            ## TODO Remove this exception once SSO supports validation of tickets
            #       generated against host machines
            # saml_token = self._get_bearer_saml_assertion_lin(request_duration, token_duration, delegatable)
        return saml_token

    def get_hok_saml_assertion(self,
                               public_key,
                               private_key,
                               request_duration=60,
                               token_duration=600,
                               act_as_token=None,
                               delegatable=False,
                               renewable=False,
                               ssl_context=None):
        '''
        Extracts the assertion from the response received from the Security
        Token Service.

        @type        public_key: C{str}
        @param       public_key: File containing the public key for the service
                                 user registered with SSO, in PEM format.
        @type       private_key: C{str}
        @param      private_key: File containing the private key for the service
                                 user registered with SSO, in PEM format.
        @type  request_duration: C{long}
        @param request_duration: The duration for which the request is valid. If
                                 the STS receives this request after this
                                 duration, it is assumed to have expired. The
                                 duration is in seconds and the default is 60s.
        @type    token_duration: C{long}
        @param   token_duration: The duration for which the SAML token is issued
                                 for. The duration is specified in seconds and
                                 the default is 600s.
        @type      act_as_token: C{str}
        @param     act_as_token: Bearer/Hok token which is delegatable
        @type       delegatable: C{boolean}
        @param      delegatable: Whether the generated token is delegatable or not
        @type         renewable: C{boolean}
        @param        renewable: Whether the generated token is renewable or not
                                 The default value is False
        @type       ssl_context: C{ssl.SSLContext}
        @param      ssl_context: SSL context describing the various SSL options.
                                 It is only supported in Python 2.7.9 or higher.
        @rtype: C{str}
        @return: The SAML assertion in Unicode.
        '''
        request = SecurityTokenRequest(public_key=public_key,
                                       private_key=private_key,
                                       request_duration=request_duration,
                                       token_duration=token_duration)
        soap_message = request.construct_hok_request(delegatable=delegatable,
                                                     act_as_token=act_as_token,
                                                     renewable=renewable)
        hok_token = self.perform_request(soap_message,
                                         public_key,
                                         private_key,
                                         ssl_context)
        return etree.tostring(
            _extract_element(
                etree.fromstring(hok_token),
                'Assertion',
                {'saml2': "urn:oasis:names:tc:SAML:2.0:assertion"}),
            pretty_print=False).decode(UTF_8)

    def get_token_by_token(self,
                           hok_token,
                           private_key,
                           request_duration=60,
                           token_duration=600,
                           delegatable=False,
                           renewable=False,
                           ssl_context=None):
        """
        Get Hok token by Hok token.

        @type       hok_token:   C{str}
        @param      hok_token:   Hok token to be used to get another token
        @type       private_key: C{str}
        @param      private_key: File containing the private key for the service
                                 user registered with SSO, in PEM format.
        @type  request_duration: C{long}
        @param request_duration: The duration for which the request is valid. If
                                 the STS receives this request after this
                                 duration, it is assumed to have expired. The
                                 duration is in seconds and the default is 60s.
        @type    token_duration: C{long}
        @param   token_duration: The duration for which the SAML token is issued
                                 for. The duration is specified in seconds and
                                 the default is 600s.
        @type    delegatable: C{boolean}
        @param   delegatable: Whether the generated token is delegatable or not.
                              The default value is False.
        @type         renewable: C{boolean}
        @param        renewable: Whether the generated token is renewable or not
                                 The default value is False
        @type       ssl_context: C{ssl.SSLContext}
        @param      ssl_context: SSL context describing the various SSL options.
                                 It is only supported in Python 2.7.9 or higher.
        @rtype: C{str}
        @return: The Hok SAML assertion in Unicode.
        """
        request = SecurityTokenRequest(private_key=private_key,
                                       request_duration=request_duration,
                                       token_duration=token_duration,
                                       hok_token=hok_token)
        soap_message = request.construct_hok_by_hok_request(
            delegatable=delegatable, renewable=renewable)
        soap_message = add_saml_context(serialized_request=soap_message,
                                        saml_token=hok_token,
                                        private_key_file=private_key,
                                        request_duration=request_duration)

        hok_token = self.perform_request(soap_message=soap_message,
                                         ssl_context=ssl_context)
        return etree.tostring(
            _extract_element(
                etree.fromstring(hok_token),
                'Assertion',
                {'saml2': "urn:oasis:names:tc:SAML:2.0:assertion"}),
            pretty_print=False).decode(UTF_8)

class SecurityTokenRequest(object):
    '''
    SecurityTokenRequest class handles the serialization of request to the STS
    for a SAML token.
    '''

    #pylint: disable=R0902
    def __init__(self,
                 username=None,
                 password=None,
                 public_key=None,
                 private_key=None,
                 request_duration=60,
                 token_duration=600,
                 gss_binary_token=None,
                 hok_token=None):
        '''
        Initializer for the SecurityToken Request class.

        @type          username: C{str}
        @param         username: Username for the user for which bearer token
                                 needs to be requested.
        @type          password: C{str}
        @param         password: Password for the user for which bearer token
                                 needs to be requested.
        @type        public_key: C{str}
        @param       public_key: The file containing the public key of the
                                 service account requesting the SAML token.
        @type       private_key: C{str}
        @param      private_key: The file containing the private key of the
                                 service account requesting the SAML token.
        @type  request_duration: C{long}
        @param request_duration: The duration for which the request is valid. If
                                 the STS receives this request after this
                                 duration, it is assumed to have expired. The
                                 duration is specified in seconds and default is
                                 60s.
        @type    token_duration: C{long}
        @param   token_duraiton: The duration for which the SAML token is issued
                                 for. The duration is specified in seconds and
                                 the default is 600s.
        '''
        self._timestamp_id = _generate_id()
        self._signature_id = _generate_id()
        self._request_id = _generate_id()
        self._security_token_id = _generate_id()
        current = datetime.datetime.utcnow()
        self._created = format_time(current.strftime(TIME_FORMAT))
        self._expires = format_time((current + datetime.timedelta(seconds=
                                token_duration)).strftime(TIME_FORMAT))
        self._request_expires = format_time((current + datetime.timedelta(seconds=
                                request_duration)).strftime(TIME_FORMAT))
        self._timestamp = TIMESTAMP_TEMPLATE % self.__dict__
        self._username = escape(username) if username else username
        self._password = escape(password) if password else password
        self._public_key_file = public_key
        self._private_key_file = private_key
        self._act_as_token = None
        self._renewable = str(False).lower()
        self._delegatable = str(False).lower()
        self._use_key = ""
        self._private_key = None
        self._binary_exchange = None
        self._public_key = None
        if gss_binary_token:
            self._binary_exchange =  BINARY_EXCHANGE_TEMPLATE % gss_binary_token
        #The following are populated later. Set to None here to keep in-line
        #with PEP8.
        self._binary_security_token = None
        self._hok_token = hok_token
        self._key_type = None
        self._security_token = None
        self._signature_text = None
        self._signature = None
        self._signed_info = None
        self._timestamp_digest = None
        self._signature_value = None
        self._xml_text = None
        self._xml = None
        self._request_digest = None

        #These will only be populated if requesting an HoK token.
        if self._private_key_file:
            with open(self._private_key_file) as fp:
                self._private_key = fp.read()

        if self._public_key_file:
            with open(self._public_key_file) as fp:
                self._public_key = fp.read()

    def construct_bearer_token_request(self, delegatable=False, renewable=False):
        '''
        Constructs the actual Bearer token SOAP request.

        @type  delegatable: C{boolean}
        @param delegatable: Whether the generated token is delegatable or not
        @type    renewable: C{boolean}
        @param   renewable: Whether the generated token is renewable or not
                            The default value is False
        @rtype:  C{str}
        @return: Bearer token SOAP request.
        '''
        self._key_type = "http://docs.oasis-open.org/ws-sx/ws-trust/200512/Bearer"
        self._security_token = USERNAME_TOKEN_TEMPLATE % self.__dict__
        self._delegatable = str(delegatable).lower()
        self._renewable = str(renewable).lower()
        return _canonicalize(REQUEST_TEMPLATE % self.__dict__)

    def construct_bearer_token_request_with_binary_token(self,
                                                         delegatable=False,
                                                         renewable=False):
        '''
        Constructs the actual Bearer token SOAP request using the binary exchange GSS/SSPI token.

        @type  delegatable: C{boolean}
        @param delegatable: Whether the generated token is delegatable or not
        @type    renewable: C{boolean}
        @param   renewable: Whether the generated token is renewable or not
                            The default value is False
        @rtype:  C{str}
        @return: Bearer token SOAP request.
        '''
        self._key_type = "http://docs.oasis-open.org/ws-sx/ws-trust/200512/Bearer"
        self._delegatable = str(delegatable).lower()
        self._renewable = str(renewable).lower()
        return _canonicalize(GSS_REQUEST_TEMPLATE % self.__dict__)

    def construct_hok_request(self, delegatable=False, act_as_token=None,
                              renewable=False):
        '''
        Constructs the actual HoK token SOAP request.

        @type   delegatable: C{boolean}
        @param  delegatable: Whether the generated token is delegatable or not
        @type  act_as_token: C{str}
        @param act_as_token: Bearer/Hok token which is delegatable
        @type    renewable: C{boolean}
        @param   renewable: Whether the generated token is renewable or not
                            The default value is False
        @rtype: C{str}
        @return: HoK token SOAP request in Unicode.
        '''
        self._binary_security_token = base64.b64encode(
            _extract_certificate(self._public_key)).decode(UTF_8)
        self._use_key = USE_KEY_TEMPLATE % self.__dict__
        self._security_token = BINARY_SECURITY_TOKEN_TEMPLATE % self.__dict__
        self._key_type = "http://docs.oasis-open.org/ws-sx/ws-trust/200512/PublicKey"
        self._renewable = str(renewable).lower()
        self._delegatable = str(delegatable).lower()
        self._act_as_token = act_as_token
        if act_as_token is None:
            self._xml_text = _canonicalize(REQUEST_TEMPLATE % self.__dict__)
        else:
            self._xml_text = ACTAS_REQUEST_TEMPLATE % self.__dict__
        self.sign_request()
        return etree.tostring(self._xml, pretty_print=False).decode(UTF_8)

    def construct_hok_by_hok_request(self, delegatable=False, renewable=False):
        """
        @type    delegatable: C{boolean}
        @param   delegatable: Whether the generated token is delegatable or not
                            The default value is False
        @type    renewable: C{boolean}
        @param   renewable: Whether the generated token is renewable or not
                            The default value is False
        @rtype: C{str}
        @return: HoK token SOAP request in Unicode.
        """
        self._delegatable = str(delegatable).lower()
        self._renewable = str(renewable).lower()
        self._key_type = "http://docs.oasis-open.org/ws-sx/ws-trust/200512/PublicKey"
        return _canonicalize(REQUEST_TEMPLATE_TOKEN_BY_TOKEN) % self.__dict__

    def sign_request(self):
        '''
        Calculates the signature to the header of the SOAP request which can be
        used by the STS to verify that the SOAP message originated from a
        trusted service.
        '''
        base_xml = etree.fromstring(self._xml_text)
        request_tree = _extract_element(base_xml,
                            'Body',
                            {'SOAP-ENV': "http://schemas.xmlsoap.org/soap/envelope/"})
        request = _canonicalize(etree.tostring(request_tree))
        request_tree = _extract_element(base_xml,
                            'Timestamp',
                            {'ns3': "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"})
        timestamp = _canonicalize(etree.tostring(request_tree))
        self._request_digest = _make_hash(request.encode(UTF_8)).decode(UTF_8)  # pylint: disable=W0612
        self._timestamp_digest = _make_hash(timestamp.encode(UTF_8)).decode(UTF_8)  # pylint: disable=W0612
        self._algorithm = SHA256
        self._signed_info = _canonicalize(SIGNED_INFO_TEMPLATE % self.__dict__)
        self._signature_value = _sign(self._private_key, self._signed_info).decode(UTF_8)
        self._signature_text = _canonicalize(SIGNATURE_TEMPLATE % self.__dict__)
        self.embed_signature()

    def embed_signature(self):
        '''
        Embeds the signature in to the header of the SOAP request.
        '''
        self._xml = etree.fromstring(self._xml_text)
        security = _extract_element(self._xml,
                                   'Security',
                                   {'ns6': "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"})
        self._signature = etree.fromstring(self._signature_text)
        security.append(self._signature)
        self._xml_text = etree.tostring(self._xml).decode(UTF_8)


def add_saml_context(serialized_request, saml_token, private_key_file, request_duration=60):
    '''
    A helper method provided to sign the outgoing LoginByToken requests with the
    HoK token.

    @type       serialized_request: C{str}
    @param      serialized_request: SOAP request which needs to be signed.
    @type               saml_token: C{str}
    @param              saml_token: SAML assertion that will be added to the SOAP
                                    request.
    @type         private_key_file: C{str}
    @param        private_key_file: Private key of the service user that will be
                                    used to sign the request, in PEM format.
    @type         request_duration: C{long}
    @param request_duration: The duration for which the request is valid. If
                                 the STS receives this request after this
                                 duration, it is assumed to have expired. The
                                 duration is in seconds and the default is 60s.
    @rtype: C{str}
    @return: signed SOAP request in Unicode.
    '''
    with open(private_key_file) as fp:
        private_key = fp.read()
    xml = etree.fromstring(serialized_request)
    value_map = {}
    value_map['_request_id'] = _generate_id()
    request_body = _extract_element(xml,
                                  'Body',
                                  {'soapenv': "http://schemas.xmlsoap.org/soap/envelope/"})
    request_body.nsmap["wsu"] = "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
    request_body.set("{http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd}Id", value_map['_request_id'])
    value_map['_request_digest'] = _make_hash_sha512(
                                    _canonicalize(etree.tostring(request_body))
                                        .encode(UTF_8)).decode(UTF_8)
    security = _extract_element(xml,
                               'Security',
                               {'ns6': "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"})
    current = datetime.datetime.utcnow()
    value_map['_created'] = format_time(current.strftime(TIME_FORMAT))
    value_map['_request_expires'] = format_time((current + datetime.timedelta(seconds=
                                            request_duration)).strftime(TIME_FORMAT))
    value_map['_timestamp_id'] = _generate_id()
    timestamp = _canonicalize(TIMESTAMP_TEMPLATE % value_map)
    value_map['_timestamp_digest'] = _make_hash_sha512(
        timestamp.encode(UTF_8)).decode(UTF_8)

    security.append(etree.fromstring(timestamp))
    value_map['_algorithm'] = SHA512
    value_map['_signed_info'] = _canonicalize(SIGNED_INFO_TEMPLATE % value_map)
    value_map['_signature_value'] = _sign(private_key,
                                          value_map['_signed_info'],
                                          SHA512).decode(UTF_8)
    value_map['samlId'] = etree.fromstring(saml_token).get("ID")
    signature = etree.fromstring(_canonicalize(REQUEST_SIGNATURE_TEMPLATE %
                                               value_map))
    security.append(signature)
    return etree.tostring(xml, pretty_print=False).decode(UTF_8)


def _generate_id():
    '''
    An internal helper method to generate UUIDs.

    @rtype: C{str}
    @return: UUID
    '''
    return "_%s" % uuid4()


def _load_private_key(der_key):
    '''
    An internal helper to load private key.

    @type  der_key: C{str}
    @param der_key: The private key, in DER format.

    @rtype: crypto.privatekey
    @return: Loaded private key.
    '''

    # OpenSSL 0.9.8 does not handle correctly PKCS8 keys passed in DER format
    # (only PKCS1 keys are understood in DER format).

    # Unencrypted PKCS8, or PKCS1 for OpenSSL 1.0.1, PKCS1 for OpenSSL 0.9.8
    try:
        return crypto.load_privatekey(crypto.FILETYPE_ASN1, der_key, b'')
    except (crypto.Error, ValueError):
        pass
    # Unencrypted PKCS8 for OpenSSL 0.9.8, and PKCS1, just in case...
    for key_type in ('PRIVATE KEY', 'RSA PRIVATE KEY'):
        try:
            return crypto.load_privatekey(crypto.FILETYPE_PEM,
                                          '-----BEGIN ' + key_type + '-----\n' +
                                          base64.encodestring(der_key).decode(UTF_8) +
                                          '-----END ' + key_type + '-----\n',
                                          b'')
        except (crypto.Error, ValueError):
            pass
    # We could try 'ENCRYPTED PRIVATE KEY' here - but we do not know passphrase.
    raise

def _sign(private_key, data, digest=SHA256):
    '''
    An internal helper method to sign the 'data' with the 'private_key'.

    @type  private_key: C{str}
    @param private_key: The private key used to sign the 'data', in one of
                        supported formats.
    @type         data: C{str}
    @param        data: The data that needs to be signed.
    @type       digest: C{str}
    @param      digest: Digest is a str naming a supported message digest type,
                        for example 'sha256'.

    @rtype: C{str}
    @return: Signed string.
    '''
    # Convert private key in arbitrary format into DER (DER is binary format
    # so we get rid of \n / \r\n differences, and line breaks in PEM).
    pkey = _load_private_key(_extract_certificate(private_key))
    return base64.b64encode(crypto.sign(pkey, data.encode(UTF_8), digest))

def _canonicalize(xml_string):
    '''
    Given an xml string, canonicalize the string per
    U{http://www.w3.org/2001/10/xml-exc-c14n#}

    @type  xml_string: C{str}
    @param xml_string: The XML string that needs to be canonicalized.

    @rtype: C{str}
    @return: Canonicalized string in Unicode.
    '''
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.fromstring(xml_string, parser=parser).getroottree()
    string = BytesIO()
    tree.write_c14n(string, exclusive=True, with_comments=False)
    return string.getvalue().decode(UTF_8)

def _extract_element(xml, element_name, namespace):
    '''
    An internal method provided to extract an element from the given XML.

    @type           xml: C{str}
    @param          xml: The XML string from which the element will be extracted.
    @type  element_name: C{str}
    @param element_name: The element that needs to be extracted from the XML.
    @type     namespace: dict
    @param    namespace: A dict containing the namespace of the element to be
                         extracted.

    @rtype: etree element.
    @return: The extracted element.
    '''
    assert(len(namespace) == 1)
    result = xml.xpath("//%s:%s" % (list(namespace.keys())[0], element_name),
                                    namespaces=namespace)
    if result:
        return result[0]
    else:
        raise KeyError("%s does not seem to be present in the XML." %
                       element_name)


def _make_hash(data):
    '''
    An internal method to calculate the sha256 hash of the data.

    @type  data: C{str}
    @param data: The data for which the hash needs to be calculated.

    @rtype: C{str}
    @return: Base64 encoded sha256 hash.
    '''
    return base64.b64encode(hashlib.sha256(data).digest())  # pylint: disable=E1101


def _make_hash_sha512(data):
    '''
    An internal method to calculate the sha512 hash of the data.

    @type  data:      C{str}
    @param data:      The data for which the hash needs to be calculated.

    @rtype: C{str}
    @return: Base64 encoded sha512 hash.
    '''
    return base64.b64encode(hashlib.sha512(data).digest())  # pylint: disable=E1101


TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

#The SAML token requests usually contain an xmldsig which guarantees that the
#message hasn't been tampered with during the transport. The following
#SIGNED_INFO_TEMPLATE is used to construct the signedinfo part of the signature.
SIGNED_INFO_TEMPLATE = """\
<ds:SignedInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
<ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-%(_algorithm)s"/>
<ds:Reference URI="#%(_request_id)s">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#%(_algorithm)s"/>
<ds:DigestValue>%(_request_digest)s</ds:DigestValue>
</ds:Reference>
<ds:Reference URI="#%(_timestamp_id)s">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#%(_algorithm)s"/>
<ds:DigestValue>%(_timestamp_digest)s</ds:DigestValue>
</ds:Reference>
</ds:SignedInfo>
"""

#The following template is used as the container for signed info in WS-Trust
#SOAP requests signed with the SAML token. It contains the digest of the
#signed info, signed with the private key of the Solution user and contains a
#reference to the actual SAML token which contains the solution user's public
#key.
REQUEST_SIGNATURE_TEMPLATE = """\
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
%(_signed_info)s
<ds:SignatureValue>%(_signature_value)s</ds:SignatureValue>
<ds:KeyInfo>
<ns2:SecurityTokenReference xmlns:ns2="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                            xmlns:wsse11="http://docs.oasis-open.org/wss/oasis-wss-wssecurity-secext-1.1.xsd"
                            wsse11:TokenType="http://docs.oasis-open.org/wss/oasis-wss-saml-token-profile-1.1#SAMLV2.0">
<ns2:KeyIdentifier ValueType="http://docs.oasis-open.org/wss/oasis-wss-saml-token-profile-1.1#SAMLID">%(samlId)s</ns2:KeyIdentifier>
</ns2:SecurityTokenReference>
</ds:KeyInfo>
</ds:Signature>"""

#The following template is used as a signed info container for the actual SAML
#token requests requesting a SAML token. It contains the digest of the signed
#info signed with the Service User's private key.
SIGNATURE_TEMPLATE = """\
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#" Id="%(_signature_id)s">
%(_signed_info)s
<ds:SignatureValue>%(_signature_value)s</ds:SignatureValue>
<ds:KeyInfo>
<ns2:SecurityTokenReference xmlns:ns2="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<ns2:Reference URI="#%(_security_token_id)s" ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"/>
</ns2:SecurityTokenReference>
</ds:KeyInfo>
</ds:Signature>"""

#The following template is used to construct the token requests to the STS.
REQUEST_TEMPLATE = """\
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
<SOAP-ENV:Header>
<ns6:Security xmlns="http://docs.oasis-open.org/ws-sx/ws-trust/200512"
              xmlns:ns2="http://www.w3.org/2005/08/addressing"
              xmlns:ns3="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
              xmlns:ns6="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
%(_timestamp)s
%(_security_token)s
</ns6:Security>
</SOAP-ENV:Header>
<SOAP-ENV:Body xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="%(_request_id)s">
<RequestSecurityToken xmlns="http://docs.oasis-open.org/ws-sx/ws-trust/200512"
                      xmlns:ns2="http://www.w3.org/2005/08/addressing"
                      xmlns:ns3="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
                      xmlns:ns6="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<TokenType>urn:oasis:names:tc:SAML:2.0:assertion</TokenType>
<RequestType>http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue</RequestType>
<Lifetime>
<ns3:Created>%(_created)s</ns3:Created>
<ns3:Expires>%(_expires)s</ns3:Expires>
</Lifetime>
<Renewing Allow="%(_renewable)s" OK="%(_renewable)s"/>
<Delegatable>%(_delegatable)s</Delegatable>
<KeyType>%(_key_type)s</KeyType>
<SignatureAlgorithm>http://www.w3.org/2001/04/xmldsig-more#rsa-sha256</SignatureAlgorithm>%(_use_key)s</RequestSecurityToken>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""

#The following template is used to construct the token-by-token requests to the STS.
REQUEST_TEMPLATE_TOKEN_BY_TOKEN = """\
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
<SOAP-ENV:Header>
<ns5:Security xmlns="http://docs.oasis-open.org/ws-sx/ws-trust/200512"
              xmlns:ns3="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
              xmlns:ns5="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
%(_hok_token)s
</ns5:Security>
</SOAP-ENV:Header>
<SOAP-ENV:Body xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="%(_request_id)s">
<RequestSecurityToken xmlns="http://docs.oasis-open.org/ws-sx/ws-trust/200512"
                      xmlns:ns3="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
<TokenType>urn:oasis:names:tc:SAML:2.0:assertion</TokenType>
<RequestType>http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue</RequestType>
<Lifetime>
<ns3:Created>%(_created)s</ns3:Created>
<ns3:Expires>%(_expires)s</ns3:Expires>
</Lifetime>
<Renewing Allow="%(_renewable)s" OK="%(_renewable)s"/>
<Delegatable>%(_delegatable)s</Delegatable>
<KeyType>%(_key_type)s</KeyType>
<SignatureAlgorithm>http://www.w3.org/2001/04/xmldsig-more#rsa-sha256</SignatureAlgorithm>
</RequestSecurityToken>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""

GSS_REQUEST_TEMPLATE = """\
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
<SOAP-ENV:Header>
<ns6:Security xmlns="http://docs.oasis-open.org/ws-sx/ws-trust/200512"
              xmlns:ns2="http://www.w3.org/2005/08/addressing"
              xmlns:ns3="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
              xmlns:ns6="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
%(_timestamp)s
</ns6:Security>
</SOAP-ENV:Header>
<SOAP-ENV:Body xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="%(_request_id)s">
<RequestSecurityToken xmlns="http://docs.oasis-open.org/ws-sx/ws-trust/200512"
                      xmlns:ns2="http://www.w3.org/2005/08/addressing"
                      xmlns:ns3="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
                      xmlns:ns6="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<TokenType>urn:oasis:names:tc:SAML:2.0:assertion</TokenType>
<RequestType>http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue</RequestType>
<Lifetime>
<ns3:Created>%(_created)s</ns3:Created>
<ns3:Expires>%(_expires)s</ns3:Expires>
</Lifetime>
<Renewing Allow="%(_renewable)s" OK="%(_renewable)s"/>
<Delegatable>%(_delegatable)s</Delegatable>
<KeyType>%(_key_type)s</KeyType>
<SignatureAlgorithm>http://www.w3.org/2001/04/xmldsig-more#rsa-sha256</SignatureAlgorithm>
%(_binary_exchange)s
%(_use_key)s</RequestSecurityToken>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""

#Template container for the service user's public key when requesting an HoK
#token.
BINARY_SECURITY_TOKEN_TEMPLATE = """\
<ns2:BinarySecurityToken xmlns:ns1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
                         xmlns:ns2="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                         EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"
                         ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"
                         ns1:Id="%(_security_token_id)s">%(_binary_security_token)s</ns2:BinarySecurityToken>
"""

#Template container for user's credentials when requesting a bearer token.
USERNAME_TOKEN_TEMPLATE = """\
<ns2:UsernameToken xmlns:ns2="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<ns2:Username>%(_username)s</ns2:Username>
<ns2:Password>%(_password)s</ns2:Password>
</ns2:UsernameToken>"""

#Template containing the anchor to the signature.
USE_KEY_TEMPLATE = """\
<UseKey Sig="%(_signature_id)s"/>"""

#The follwoing template is used to create a timestamp for the various messages.
#The timestamp is used to indicate the duration of the request itself.
TIMESTAMP_TEMPLATE = """\
<ns3:Timestamp xmlns:ns3="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" ns3:Id="%(_timestamp_id)s">
<ns3:Created>%(_created)s</ns3:Created><ns3:Expires>%(_request_expires)s</ns3:Expires></ns3:Timestamp>"""

BINARY_EXCHANGE_TEMPLATE = """\
<BinaryExchange EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary" ValueType="http://schemas.xmlsoap.org/ws/2005/02/trust/spnego">%s</BinaryExchange>"""

ACTAS_REQUEST_TEMPLATE = """<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Header><ns6:Security xmlns:ns6="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"><ns3:Timestamp xmlns:ns3="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" ns3:Id="%(_timestamp_id)s"><ns3:Created>%(_created)s</ns3:Created><ns3:Expires>%(_request_expires)s</ns3:Expires></ns3:Timestamp><ns2:BinarySecurityToken xmlns:ns1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:ns2="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary" ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" ns1:Id="%(_security_token_id)s">%(_binary_security_token)s</ns2:BinarySecurityToken></ns6:Security></SOAP-ENV:Header><SOAP-ENV:Body xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="%(_request_id)s"><RequestSecurityToken xmlns="http://docs.oasis-open.org/ws-sx/ws-trust/200512"><TokenType>urn:oasis:names:tc:SAML:2.0:assertion</TokenType><RequestType>http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue</RequestType><Lifetime><ns3:Created xmlns:ns3="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">%(_created)s</ns3:Created><ns3:Expires xmlns:ns3="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">%(_expires)s</ns3:Expires></Lifetime><Renewing Allow="%(_renewable)s" OK="%(_renewable)s"></Renewing><Delegatable>%(_delegatable)s</Delegatable><ns4:ActAs xmlns:ns4="http://docs.oasis-open.org/ws-sx/ws-trust/200802">%(_act_as_token)s</ns4:ActAs><KeyType>http://docs.oasis-open.org/ws-sx/ws-trust/200512/PublicKey</KeyType><SignatureAlgorithm>http://www.w3.org/2001/04/xmldsig-more#rsa-sha256</SignatureAlgorithm><ns3:UseKey xmlns:ns3="http://docs.oasis-open.org/ws-sx/ws-trust/200512" Sig="%(_signature_id)s"></ns3:UseKey></RequestSecurityToken></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
