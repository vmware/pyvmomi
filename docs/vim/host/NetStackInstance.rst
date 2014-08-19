
vim.host.NetStackInstance
=========================
  This class describes Network Stack Instance configuration
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key of instance For instance which created by host, its value should be SystemStackKey.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The display name
    dnsConfig (`vim.host.DnsConfig <vim/host/DnsConfig.rst>`_, optional):

       DNS configuration
    ipRouteConfig (`vim.host.IpRouteConfig <vim/host/IpRouteConfig.rst>`_, optional):

       IP Route configuration
    requestedMaxNumberOfConnections (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum number of socket connection that are requested on this instance
    congestionControlAlgorithm (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The TCP congest control algorithm used by this instance, See CongestionControlAlgorithmType for valid values.
    ipV6Enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Enable or disable IPv6 protocol on this stack instance. This property is not supported currently.
    routeTableConfig (`vim.host.IpRouteTableConfig <vim/host/IpRouteTableConfig.rst>`_, optional):

