.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _NetBIOSConfigInfoMode: ../../vim/net/NetBIOSConfigInfo/Mode.rst


vim.net.NetBIOSConfigInfo
=========================
  This data object type describes the NetBIOS configuration of an operating system.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    mode (`str`_):

       NetBIOS configuration mode. The supported values are described by `NetBIOSConfigInfoMode`_ .
