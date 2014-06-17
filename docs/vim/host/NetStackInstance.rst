.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.DnsConfig: ../../vim/host/DnsConfig.rst

.. _vim.host.IpRouteConfig: ../../vim/host/IpRouteConfig.rst

.. _vim.host.IpRouteTableConfig: ../../vim/host/IpRouteTableConfig.rst


vim.host.NetStackInstance
=========================
  This class describes Network Stack Instance configuration
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    key (`str`_, optional):

       Key of instance For instance which created by host, its value should be SystemStackKey.
    name (`str`_, optional):

       The display name
    dnsConfig (`vim.host.DnsConfig`_, optional):

       DNS configuration
    ipRouteConfig (`vim.host.IpRouteConfig`_, optional):

       IP Route configuration
    requestedMaxNumberOfConnections (`int`_, optional):

       The maximum number of socket connection that are requested on this instance
    congestionControlAlgorithm (`str`_, optional):

       The TCP congest control algorithm used by this instance, See CongestionControlAlgorithmType for valid values.
    ipV6Enabled (`bool`_, optional):

       Enable or disable IPv6 protocol on this stack instance. This property is not supported currently.
    routeTableConfig (`vim.host.IpRouteTableConfig`_, optional):

