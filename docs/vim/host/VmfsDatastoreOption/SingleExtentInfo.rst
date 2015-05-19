.. _vim.host.VmfsDatastoreOption.Info: ../../../vim/host/VmfsDatastoreOption/Info.rst

.. _vim.host.DiskPartitionInfo.BlockRange: ../../../vim/host/DiskPartitionInfo/BlockRange.rst


vim.host.VmfsDatastoreOption.SingleExtentInfo
=============================================
  Datastore addition policy to use a single extent on the disk for a VMFS datastore. A single extent implies that one disk partition will be created on the disk for creating or increasing the capacity of a VMFS datastore.
:extends: vim.host.VmfsDatastoreOption.Info_

Attributes:
    vmfsExtent (`vim.host.DiskPartitionInfo.BlockRange`_):

       The block range to be used as an extent in a VMFS datastore.
