.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.net.DhcpConfigInfo.DhcpOptions: ../../vim/net/DhcpConfigInfo/DhcpOptions.rst


vim.net.DhcpConfigInfo
======================
  Dynamic Host Configuration Protocol reporting for IP version 4 and version 6.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    ipv6 (`vim.net.DhcpConfigInfo.DhcpOptions`_, optional):

       IPv6 DHCP client settings.
    ipv4 (`vim.net.DhcpConfigInfo.DhcpOptions`_, optional):

       IPv4 DHCP client settings.
