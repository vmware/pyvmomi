
vim.Extension.ServerInfo
========================
  This data object type describes a server for the extension.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    url (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Server url.
    description (`vim.Description <vim/Description.rst>`_):

       Server description.
    company (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Company information.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Type of server (examples may include SOAP, REST, HTTP, etc.).
    adminEmail ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       Extension administrator email addresses.
    serverThumbprint (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Thumbprint of the extension server certificate presented to clients
