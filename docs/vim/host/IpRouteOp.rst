
vim.host.IpRouteOp
==================
  Routing Entry Operation. Routing entries are individual static routes which combined with the default route form all of the routing rules for a host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    changeOperation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       This property indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation <vim/host/ConfigChange/Operation.rst>`_ 
    route (`vim.host.IpRouteEntry <vim/host/IpRouteEntry.rst>`_):

       The routing entry itself
