.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.dvs.KeyedOpaqueBlob
=======================
  This class defines a data structure to hold opaque binary data identified by a key.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       A key that identifies the opaque binary blob.
    opaqueData (`str`_):

       The opaque data. It is recommended that base64 encoding be used for binary data.
