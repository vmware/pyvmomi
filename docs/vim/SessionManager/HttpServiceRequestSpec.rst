.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vim.SessionManager.ServiceRequestSpec: ../../vim/SessionManager/ServiceRequestSpec.rst

.. _SessionManagerHttpServiceRequestSpecMethod: ../../vim/SessionManager/HttpServiceRequestSpec/Method.rst


vim.SessionManager.HttpServiceRequestSpec
=========================================
  This data object type describes a request to an HTTP or HTTPS service.
:extends: vim.SessionManager.ServiceRequestSpec_
:since: `vSphere API 5.0`_

Attributes:
    method (`str`_, optional):

       The HTTP method used for the request. If null, then any method is assumed.See `SessionManagerHttpServiceRequestSpecMethod`_ 
    url (`str`_):

       URL of the HTTP request. E.g. 'https://127.0.0.1:8080/cgi-bin/vm-support.cgi?n=val'.For ESXi CGI service requests:
        * only the path and query parts of the URL are used (e.g. "/cgi-bin/vm-support.cgi?n=val").This is so because the scheme is not known to the CGI service, and the port may not be the same if using a proxy.
