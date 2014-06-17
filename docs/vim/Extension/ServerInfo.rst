.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.Description: ../../vim/Description.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.Extension.ServerInfo
========================
  This data object type describes a server for the extension.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    url (`str`_):

       Server url.
    description (`vim.Description`_):

       Server description.
    company (`str`_):

       Company information.
    type (`str`_):

       Type of server (examples may include SOAP, REST, HTTP, etc.).
    adminEmail (`str`_):

       Extension administrator email addresses.
    serverThumbprint (`str`_, optional):

       Thumbprint of the extension server certificate presented to clients
