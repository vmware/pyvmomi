.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.ScsiLun: ../../../vim/host/ScsiLun.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _SetMultipathLunPolicy: ../../../vim/host/StorageSystem.rst#setMultipathLunPolicy

.. _vim.host.MultipathInfo.Path: ../../../vim/host/MultipathInfo/Path.rst

.. _HostMultipathInfoLogicalUnit: ../../../vim/host/MultipathInfo/LogicalUnit.rst

.. _vim.host.MultipathInfo.LogicalUnitPolicy: ../../../vim/host/MultipathInfo/LogicalUnitPolicy.rst

.. _vim.host.MultipathInfo.LogicalUnitStorageArrayTypePolicy: ../../../vim/host/MultipathInfo/LogicalUnitStorageArrayTypePolicy.rst


vim.host.MultipathInfo.LogicalUnit
==================================
  The `HostMultipathInfoLogicalUnit`_ data object represents a storage entity that provides disk blocks to a host.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       Linkable identifier.
    id (`str`_):

       Identifier of LogicalUnit.Use this id to configure LogicalUnit multipathing policy using `SetMultipathLunPolicy`_ .
    lun (`vim.host.ScsiLun`_):

       SCSI device corresponding to logical unit.
    path (`vim.host.MultipathInfo.Path`_):

       Array of paths available to access this LogicalUnit.
    policy (`vim.host.MultipathInfo.LogicalUnitPolicy`_):

       Policy that the logical unit should use when selecting a path.
    storageArrayTypePolicy (`vim.host.MultipathInfo.LogicalUnitStorageArrayTypePolicy`_, optional):

       Policy used to determine how a storage device is accessed. This policy is currently immutable.
