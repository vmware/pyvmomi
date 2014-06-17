.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _MultipathState: ../../../vim/host/MultipathInfo/PathState.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _EnableMultipathPath: ../../../vim/host/StorageSystem.rst#enableMultipathPath

.. _DisableMultipathPath: ../../../vim/host/StorageSystem.rst#disableMultipathPath

.. _HostMultipathInfoPath: ../../../vim/host/MultipathInfo/Path.rst

.. _vim.host.HostBusAdapter: ../../../vim/host/HostBusAdapter.rst

.. _vim.host.TargetTransport: ../../../vim/host/TargetTransport.rst

.. _vim.host.MultipathInfo.LogicalUnit: ../../../vim/host/MultipathInfo/LogicalUnit.rst


vim.host.MultipathInfo.Path
===========================
  The `HostMultipathInfoPath`_ data object is a storage entity that represents a topological path from a host bus adapter to a SCSI logical unit. Each path is unique although each host bus adapter/SCSI logical unit pair can have multiple paths.Path objects are identified by a key. The specifics of how the key is formatted are dependent on the implementation. Example implementations include using strings like "vmhba1:0:0:0".
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       Identifier of the path.
    name (`str`_):

       Name of path.Use this name to configure LogicalUnit multipathing policy using `EnableMultipathPath`_ and `DisableMultipathPath`_ .
    pathState (`str`_):

       State of the path. Must be one of the values of `MultipathState`_ activePath can be used for I/O and is currently a working path.standbyPath can be used for I/O but is not a working path or can be used if active paths fail.disabledPath has been administratively disabled.deadPath cannot be used for I/O.unknownPath is in unknown error state.
    state (`str`_, optional):

       System-reported state of the path. Must be one of the values of `MultipathState`_ activePath can be used for I/O.standbyPath can be used for I/O if active paths fail.disabledPath has been administratively disabled.deadPath cannot be used for I/O.unknownPath is in unknown error state.
    isWorkingPath (`bool`_, optional):

       A path, managed by a given path selection policy(psp) plugin, is denoted to be a Working Path if the psp plugin is likely to select the path for performing I/O in the near future.
    adapter (`vim.host.HostBusAdapter`_):

       The host bus adapter at one endpoint of this path.
    lun (`vim.host.MultipathInfo.LogicalUnit`_):

       The logical unit at one endpoint of this path.
    transport (`vim.host.TargetTransport`_, optional):

       Transport information for the target end of the path.
