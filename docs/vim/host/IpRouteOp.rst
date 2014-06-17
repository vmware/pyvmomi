.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.IpRouteEntry: ../../vim/host/IpRouteEntry.rst

.. _HostConfigChangeOperation: ../../vim/host/ConfigChange/Operation.rst


vim.host.IpRouteOp
==================
  Routing Entry Operation. Routing entries are individual static routes which combined with the default route form all of the routing rules for a host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    changeOperation (`str`_):

       This property indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation`_ 
    route (`vim.host.IpRouteEntry`_):

       The routing entry itself
