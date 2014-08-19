
vim.host.MultipathStateInfo.Path
================================
  Data object indicating state of storage path for a named path.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of path.Use this name to enable or disable storage paths `EnableMultipathPath <vim/host/StorageSystem.rst#enableMultipathPath>`_ and `DisableMultipathPath <vim/host/StorageSystem.rst#disableMultipathPath>`_ .In addition to being the identifier for the path state operations, the name is used to correlate this object to the corresponding Path object in other contexts.See `name <vim/host/PlugStoreTopology/Path.rst#name>`_ 
    pathState (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The state of the path. Must be one of the values of `MultipathState <vim/host/MultipathInfo/PathState.rst>`_ .
