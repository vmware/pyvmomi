
vim.SessionManager.HttpServiceRequestSpec
=========================================
  This data object type describes a request to an HTTP or HTTPS service.
:extends: vim.SessionManager.ServiceRequestSpec_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    method (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The HTTP method used for the request. If null, then any method is assumed.See `SessionManagerHttpServiceRequestSpecMethod <vim/SessionManager/HttpServiceRequestSpec/Method.rst>`_ 
    url (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       URL of the HTTP request. E.g. 'https://127.0.0.1:8080/cgi-bin/vm-support.cgi?n=val'.For ESXi CGI service requests:
        * only the path and query parts of the URL are used (e.g. "/cgi-bin/vm-support.cgi?n=val").This is so because the scheme is not known to the CGI service, and the port may not be the same if using a proxy.
