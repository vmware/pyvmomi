.. _str: https://docs.python.org/2/library/stdtypes.html

.. _name: ../../../vim/host/PlugStoreTopology/Path.rst#name

.. _MultipathState: ../../../vim/host/MultipathInfo/PathState.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _EnableMultipathPath: ../../../vim/host/StorageSystem.rst#enableMultipathPath

.. _DisableMultipathPath: ../../../vim/host/StorageSystem.rst#disableMultipathPath


vim.host.MultipathStateInfo.Path
================================
  Data object indicating state of storage path for a named path.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    name (`str`_):

       Name of path.Use this name to enable or disable storage paths `EnableMultipathPath`_ and `DisableMultipathPath`_ .In addition to being the identifier for the path state operations, the name is used to correlate this object to the corresponding Path object in other contexts.See `name`_ 
    pathState (`str`_):

       The state of the path. Must be one of the values of `MultipathState`_ .
