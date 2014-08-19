
vim.host.VmfsDatastoreExpandSpec
================================
  Specification to increase the capacity of a VMFS datastore by expanding (increasing the size of) an existing extent of the datastore.
:extends: vim.host.VmfsDatastoreSpec_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    partition (`vim.host.DiskPartitionInfo.Specification <vim/host/DiskPartitionInfo/Specification.rst>`_):

       Partitioning specification.
    extent (`vim.host.ScsiDisk.Partition <vim/host/ScsiDisk/Partition.rst>`_):

       VMFS extent to expand.
