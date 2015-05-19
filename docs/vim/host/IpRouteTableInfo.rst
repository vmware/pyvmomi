.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.IpRouteEntry: ../../vim/host/IpRouteEntry.rst


vim.host.IpRouteTableInfo
=========================
  IpRouteTableInfo. This is the list of all static routes on the host
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    ipRoute ([`vim.host.IpRouteEntry`_], optional):

       The array of IpRouteEntry
    ipv6Route ([`vim.host.IpRouteEntry`_], optional):

