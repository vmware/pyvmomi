.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.LowLevelProvisioningManager.DiskLayoutSpec: ../../../vim/host/LowLevelProvisioningManager/DiskLayoutSpec.rst


vim.host.LowLevelProvisioningManager.SnapshotLayoutSpec
=======================================================
  File layout spec of a snapshot, including path to the vmsn file of the snapshot and the layout of virtual disks when the snapshot was taken.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    id (`int`_):

       The unique identifier of the snapshot
    srcFilename (`str`_):

       Name of the source snapshot file in datastore path.
    dstFilename (`str`_):

       Name of the destination snapshot file in datastore path.
    disk ([`vim.host.LowLevelProvisioningManager.DiskLayoutSpec`_], optional):

       Layout of each virtual disk of the virtual machine when the snapshot was taken.
