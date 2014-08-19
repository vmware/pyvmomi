
vim.host.MultipathInfo.LogicalUnit
==================================
  The `HostMultipathInfoLogicalUnit <vim/host/MultipathInfo/LogicalUnit.rst>`_ data object represents a storage entity that provides disk blocks to a host.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Linkable identifier.
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Identifier of LogicalUnit.Use this id to configure LogicalUnit multipathing policy using `SetMultipathLunPolicy <vim/host/StorageSystem.rst#setMultipathLunPolicy>`_ .
    lun (`vim.host.ScsiLun <vim/host/ScsiLun.rst>`_):

       SCSI device corresponding to logical unit.
    path ([`vim.host.MultipathInfo.Path <vim/host/MultipathInfo/Path.rst>`_]):

       Array of paths available to access this LogicalUnit.
    policy (`vim.host.MultipathInfo.LogicalUnitPolicy <vim/host/MultipathInfo/LogicalUnitPolicy.rst>`_):

       Policy that the logical unit should use when selecting a path.
    storageArrayTypePolicy (`vim.host.MultipathInfo.LogicalUnitStorageArrayTypePolicy <vim/host/MultipathInfo/LogicalUnitStorageArrayTypePolicy.rst>`_, optional):

       Policy used to determine how a storage device is accessed. This policy is currently immutable.
