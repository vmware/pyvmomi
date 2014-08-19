
vim.host.InternetScsiHba.DigestCapabilities
===========================================
  The digest capabilities for this host bus adapter.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    headerDigestSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if this host bus adapter supports the configuration of the use of header digest. Defaults to false, in which case no header digests will be used.
    dataDigestSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if this host bus adapter supports the configuration of the use of data digest. Defaults to false, in which case no data digests will be used.
    targetHeaderDigestSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if configuration of the use of header digest is supported on the targets associated with the host bus adapter. Defaults to false, in which case no header digests will be used.
    targetDataDigestSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if configuration of the use of data digest is supported on the targets associated with the host bus adapter. Defaults to false, in which case no data digests will be used.
