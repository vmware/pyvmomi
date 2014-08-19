
vim.host.VmfsDatastoreExtendSpec
================================
  Specification to increase the capacity of a VMFS datastore by adding one or more new extents to the datastore. All the extents to be added must be on the same disk. Extension is different from creation in that the VMFS creation specification need not be specified.
:extends: vim.host.VmfsDatastoreSpec_

Attributes:
    partition (`vim.host.DiskPartitionInfo.Specification <vim/host/DiskPartitionInfo/Specification.rst>`_):

       Partitioning specification.
    extent ([`vim.host.ScsiDisk.Partition <vim/host/ScsiDisk/Partition.rst>`_]):

       Extents to append to VMFS.
