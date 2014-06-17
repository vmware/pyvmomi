.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostDigestInfoDigestMethodType: ../../vim/host/DigestInfo/DigestMethodType.rst


vim.host.DigestInfo
===================
  This data object type describes the digest information
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    digestMethod (`str`_):

       Method in which the digest value is calculated. The set of possible values is described in `HostDigestInfoDigestMethodType`_ .
    digestValue (`int`_):

       The variable length byte array containing the digest value calculated by the specified digestMethod.
    objectName (`str`_, optional):

       The name of the object from which this digest value is calcaulated.
