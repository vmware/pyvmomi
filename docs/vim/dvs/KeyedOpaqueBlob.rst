
vim.dvs.KeyedOpaqueBlob
=======================
  This class defines a data structure to hold opaque binary data identified by a key.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A key that identifies the opaque binary blob.
    opaqueData (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The opaque data. It is recommended that base64 encoding be used for binary data.
