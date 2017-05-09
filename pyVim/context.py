# VMware vSphere Python SDK
# Copyright (c) 2008-2017 VMware, Inc. All Rights Reserved.
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

__author__ = "VMware, Inc."

from pyVim import connect

class Connection():
    """
    A context connection object for use with pyVmomi that is thread-safe and multi-processor safe.
    Upon leaving the context the session will be properly closed without impacting any other
    potentially open sessions.

    :Example:
    from pyVim import context
    
    with context.Connection(host='my_host', pwd='my_password') as si:
        server_time = si.CurrentTime()
        print server_time

    """
    def __init__(self, host='localhost', port=443, user='root', pwd='',
            service="hostd", adapter="SOAP", namespace=None, path="/sdk",
            version=None, keyFile=None, certFile=None, thumbprint=None,
            sslContext=None, b64token=None, mechanism='userpass'):
        """
        Most values are optional. Specify the minimum values for your use case.
        :param host: default 'localhost' specify your host here
        :param port: default '443' specify only if different
        :param user: default 'root' specify only if needed
        :param pwd: default '' specify only if different
        :param service: defaults to 'hostd' specify only if you need to
        :param adapter: defaults to SOAP specify only if required to do so
        :param namespace: default will be calculated on connection
        :param path: defaults to /sdk only specify if you must
        :param version: default calculates the highest version number SDK + Host can use together
        :param keyFile: specify only if using self-signed PEM key files
        :param certFile: specify only if using self-signed certs
        :param thumbprint: specify only if overriding based on known SSL thumbprints
        :param sslContext: specify only if you are overriding default SSL context behaviors
        :param b64token: specify if you have a Token such as the HoK Token
        :param mechanism: specify as either 'userpass' or 'sspi'
        """
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.service = service
        self.adapter=adapter
        self.namespace=namespace
        self.path=path
        self.version=version
        self.keyFile=keyFile
        self.certFile=certFile
        self.thumbprint=thumbprint
        self.sslContext=sslContext
        self.b64token=b64token
        self.mechanism=mechanism

    def __enter__(self):
        self.si = Connection.open(host=self.host,port=self.port,user=self.user,pwd=self.pwd,service=self.service,
                       adapter=self.adapter,namespace=self.namespace,path=self.path,version=self.version,
                       keyFile=self.keyFile,certFile=self.certFile,thumbprint=self.thumbprint,
                       sslContext=self.sslContext, b64token=self.b64token, mechanism=self.mechanism)
        return self.si

    def __exit__(self, *args):
        Connection.close(self.si)
        return

    @staticmethod
    def open(host='localhost', port=443, user='root', pwd='',
             service="hostd", adapter="SOAP", namespace=None, path="/sdk",
             version=None, keyFile=None, certFile=None, thumbprint=None,
             sslContext=None, b64token=None, mechanism='userpass'):
        """
        Parallel processing friendly version of connect creates a new service instance on each call. This means you have
        to be very careful to close the session in your process or else you will create orphaned sessions on the server.

        :param host: vSphere host to connect to
        :param port: port number if not 443
        :param user: username if not root
        :param pwd: password if not blank
        :param service: service name if not hostd
        :param adapter: adapter type if not SOAP
        :param namespace: namespace if not None or global default namespace
        :param path: if not the default /sdk specify here
        :param version: specify a version if not the server's default
        :param keyFile: specify a special SSL key file here
        :param certFile: specify a special cert file here
        :param thumbprint: allow a thumbprint override
        :param sslContext: or ... optionally define an SSL context
        :param b64token: or ... define a base 64 key token (ie: HOK token)
        :param mechanism: either the default username/password as 'userpass' or 'sspi'
        :return: your own copy of a session instance ... remember to close when finished!
        """
        try:
            info = connect.re.match(connect._rx, host)
            if info is not None:
                host = info.group(1)
                if host[0] == '[':
                    host = info.group(1)[1:-1]
                if info.group(2) is not None:
                    port = int(info.group(2)[1:])
        except ValueError as ve:
            pass

        sslContext = connect.localSslFixup(host, sslContext)

        if namespace:
            assert (version is None)
            version = connect.versionMap[namespace]
        elif not version:
            version = "vim.version.version6"


        si, stub = None, None
        if mechanism == 'userpass':
            si, stub = connect.__Login(host, port, user, pwd, service, adapter, version, path,
                                       keyFile, certFile, thumbprint, sslContext)
        elif mechanism == 'sspi':
            si, stub = connect.__LoginBySSPI(host, port, service, adapter, version, path,
                                             keyFile, certFile, thumbprint, sslContext, b64token)
        else:
            raise Exception('''The provided connection mechanism is not available, the
                      supported mechanisms are userpass or sspi''')


        return si

    @staticmethod
    def close(si):
        """

        :param si: the session instance aka connection instance
        :return:
        """
        try:
            if si:
                content = si.RetrieveContent()
                content.sessionManager.Logout()
        except Exception as e:
            pass

        return


