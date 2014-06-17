.. _vim.host.VmfsDatastoreSpec: ../../vim/host/VmfsDatastoreSpec.rst

.. _vim.host.ScsiDisk.Partition: ../../vim/host/ScsiDisk/Partition.rst

.. _vim.host.VmfsVolume.Specification: ../../vim/host/VmfsVolume/Specification.rst

.. _vim.host.DiskPartitionInfo.Specification: ../../vim/host/DiskPartitionInfo/Specification.rst


vim.host.VmfsDatastoreCreateSpec
================================
  This data object type is used when creating a new VMFS datastore, to create a specification for the VMFS datastore.
:extends: vim.host.VmfsDatastoreSpec_

Attributes:
    partition (`vim.host.DiskPartitionInfo.Specification`_):

       Partitioning specification.
    vmfs (`vim.host.VmfsVolume.Specification`_):

       The VMFS creation specification.
    extent (`vim.host.ScsiDisk.Partition`_, optional):

       Extents to append to VMFS.
