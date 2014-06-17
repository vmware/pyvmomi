.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.host.VmfsDatastoreSpec: ../../vim/host/VmfsDatastoreSpec.rst

.. _vim.host.ScsiDisk.Partition: ../../vim/host/ScsiDisk/Partition.rst

.. _vim.host.DiskPartitionInfo.Specification: ../../vim/host/DiskPartitionInfo/Specification.rst


vim.host.VmfsDatastoreExpandSpec
================================
  Specification to increase the capacity of a VMFS datastore by expanding (increasing the size of) an existing extent of the datastore.
:extends: vim.host.VmfsDatastoreSpec_
:since: `vSphere API 4.0`_

Attributes:
    partition (`vim.host.DiskPartitionInfo.Specification`_):

       Partitioning specification.
    extent (`vim.host.ScsiDisk.Partition`_):

       VMFS extent to expand.
