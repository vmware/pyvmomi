
vim.host.PlugStoreTopology.Plugin
=================================
  This data object type represents a Plugin in the plug store architecture. A Plugin claims a set of paths and groups them into Devices.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The identifier of the plugin.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the plugin.
    device ([`vim.host.PlugStoreTopology.Device <vim/host/PlugStoreTopology/Device.rst>`_], optional):

       The set of devices formed by this plugin.
    claimedPath ([`vim.host.PlugStoreTopology.Path <vim/host/PlugStoreTopology/Path.rst>`_], optional):

       The set of paths claimed by this plugin. Not every claimed path will necessarily appear as part of a Device. Claimed paths will only appear under Devices if the device identifier of the path matches up with the device identifier exposed by the Device.
