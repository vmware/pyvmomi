.. _vim.KeyValue: ../../../vim/KeyValue.rst

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.net.DnsConfigInfo: ../../../vim/net/DnsConfigInfo.rst

.. _vim.net.DhcpConfigInfo: ../../../vim/net/DhcpConfigInfo.rst

.. _vim.net.IpRouteConfigInfo: ../../../vim/net/IpRouteConfigInfo.rst


vim.vm.GuestInfo.StackInfo
==========================
  Information about the Internet Protocol stack as configured in the guest operating system.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    dnsConfig (`vim.net.DnsConfigInfo`_, optional):

       Client DNS configuration. How DNS queries are resolved.
    ipRouteConfig (`vim.net.IpRouteConfigInfo`_, optional):

       IP route table configuration.
    ipStackConfig (`vim.KeyValue`_, optional):

       Report Kernel IP configuration settings. The key part contains a unique number in the report. The value part contains the 'key=value' as provided by the underlying provider. For example on Linux, BSD, the systcl -a output would be reported as: key='5', value='net.ipv4.tcp_keepalive_time = 7200'
    dhcpConfig (`vim.net.DhcpConfigInfo`_, optional):

       Client side DHCP for a given interface. This reports only the system wide dhcp client settings. See NicInfo.IpConfig for per interface settings. For example on Linux, BSD systems: Using the file dhclient.conf output would be reported as: key='1', value='timeout 60;' key='2', value='reboot 10;'
