
vim.Extension.ClientInfo
========================
  This data object type describes a client of the extension.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Client version number as a dot-separated string. For example, "1.0.0"
    description (`vim.Description <vim/Description.rst>`_):

       Description of client.
    company (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Company information.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Type of client (examples may include win32, .net, linux, etc.).
    url (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Plugin url.
