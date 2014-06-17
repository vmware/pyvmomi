.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.KeyValue: ../../../vim/KeyValue.rst

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.net.DhcpConfigInfo.DhcpOptions
==================================
  Provides for reporting of DHCP client. This data object may be used at a per interface or per system scope.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    enable (`bool`_):

       Report state of dhcp client services.
    config (`vim.KeyValue`_, optional):

       Platform specific settings for DHCP Client. The key part is a unique number, the value part is the platform specific configuration command. For example on Linux, BSD systems using the file dhclient.conf output would be reported at system scope: key='1', value='timeout 60;' key='2', value='reboot 10;' output reported at per interface scope: key='1', value='prepend domain-name-servers 192.0.2.1;' key='2', value='equire subnet-mask, domain-name-servers;'
