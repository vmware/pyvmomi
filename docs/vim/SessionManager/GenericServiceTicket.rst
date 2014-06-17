.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _SessionManagerServiceRequestSpec: ../../vim/SessionManager/ServiceRequestSpec.rst


vim.SessionManager.GenericServiceTicket
=======================================
  This data object represents a ticket which grants access to some service. The ticket may be used only once and is valid only for the `SessionManagerServiceRequestSpec`_ with which it was acquired. For HTTP service requests (when spec is of type HttpServiceRequestSpec) the returned ticket must be used by setting `id`_ as the value of a special cookie in the HTTP request. For CGI requests the name of this cookie is 'vmware_cgi_ticket'. The use of the returned ticket for other services is to be defined.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    id (`str`_):

       A unique string identifying the ticket.
    hostName (`str`_, optional):

       The name of the host that the service is running on
    sslThumbprint (`str`_, optional):

       The expected thumbprint of the SSL certificate of the host. If it is empty, the host must be authenticated by name.
