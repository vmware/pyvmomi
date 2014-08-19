
vim.host.PlugStoreTopology.Adapter
==================================
  This data object type is an association class that describes a host bus adapter and its associated storage Paths. The set of Paths on all the host bus adapters is the complete set of Paths in the system.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The identifier for the host bus adapter.
    adapter (`vim.host.HostBusAdapter <vim/host/HostBusAdapter.rst>`_):

       The link to the host bus adapter for this inebtrface.
    path ([`vim.host.PlugStoreTopology.Path <vim/host/PlugStoreTopology/Path.rst>`_], optional):

       The list of paths to which the host bus adapter is associated.
