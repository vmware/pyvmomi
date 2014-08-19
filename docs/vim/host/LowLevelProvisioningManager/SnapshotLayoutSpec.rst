
vim.host.LowLevelProvisioningManager.SnapshotLayoutSpec
=======================================================
  File layout spec of a snapshot, including path to the vmsn file of the snapshot and the layout of virtual disks when the snapshot was taken.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    id (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The unique identifier of the snapshot
    srcFilename (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the source snapshot file in datastore path.
    dstFilename (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the destination snapshot file in datastore path.
    disk ([`vim.host.LowLevelProvisioningManager.DiskLayoutSpec <vim/host/LowLevelProvisioningManager/DiskLayoutSpec.rst>`_], optional):

       Layout of each virtual disk of the virtual machine when the snapshot was taken.
