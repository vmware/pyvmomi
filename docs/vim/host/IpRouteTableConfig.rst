.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.IpRouteOp: ../../vim/host/IpRouteOp.rst


vim.host.IpRouteTableConfig
===========================
  IpRouteEntry. Routing entries are individual static routes which combined with the default route form all of the routing rules for a host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    ipRoute ([`vim.host.IpRouteOp`_], optional):

       The array of Routing ops (routes to be added/removed)
    ipv6Route ([`vim.host.IpRouteOp`_], optional):

