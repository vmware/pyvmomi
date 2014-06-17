.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.KeyValue: ../../../vim/KeyValue.rst

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _NetDhcpConfigInfo: ../../../vim/net/DhcpConfigInfo.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostConfigChangeOperation: ../../../vim/host/ConfigChange/Operation.rst


vim.net.DhcpConfigSpec.DhcpOptionsSpec
======================================
  Provides for configuration of IPv6
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    enable (`bool`_, optional):

       Enable or disable dhcp for IPv4.
    config (`vim.KeyValue`_):

       Platform specific settings for DHCP Client. The key part is a unique number, the value part is the platform specific configuration command. See `NetDhcpConfigInfo`_ for value formatting.
    operation (`str`_):

       Requires one of the values from `HostConfigChangeOperation`_ .
