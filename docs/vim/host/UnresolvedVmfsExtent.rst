
vim.host.UnresolvedVmfsExtent
=============================
  Information about an unresolved VMFS volume extent An unresolved VMFS volume extent is a device partition which is detected to have copy of an extent of a VMFS volume. Such a copy can be created via replication or snapshots, for example.See `HostUnresolvedVmfsVolume <vim/host/UnresolvedVmfsVolume.rst>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    device (`vim.host.ScsiDisk.Partition <vim/host/ScsiDisk/Partition.rst>`_):

       The device information
    devicePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The device path of an VMFS extent
    vmfsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The UUID of the VMFS volume read from to the partition.
    isHeadExtent (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Is this a copy of the head extent of the VMFS volume?
    ordinal (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       A number indicating the order of an extent in a volume. An extent with a lower ordinal value than another extent provides a range of blocks to a volume at an earlier block address range. Extents with the same ordinal provide the same range of blocks to a volume. A zero ordinal indicates that the extent is a head extent.In the case each extent in the `HostUnresolvedVmfsVolume <vim/host/UnresolvedVmfsVolume.rst>`_ is represented in the list of `HostUnresolvedVmfsExtent <vim/host/UnresolvedVmfsExtent.rst>`_ data objects, the ordinal will refer to the absolute index of the extent in the volume. For example, ordinal "1" refers to the second extent; ordinal "2" refers to the third extent.In the case that some extents of the volume are not represented in the `HostUnresolvedVmfsExtent <vim/host/UnresolvedVmfsExtent.rst>`_ list, the ordinal will not precisely describe the position in the list of extents. A number will be skipped to indicate holes in the extent order. For example, given a volume with five extents with the second and third extents missing, the ordinal values in use will be {0, 2, 3}. The missing second and third extent are represented by the missing ordinal value "1" while the fourth and fifth extents will be assigned an ordinal of "2" and "3" respectively.The reason the ordinals are not reliable in the case of missing extents is because the extents are identified by their start and end blocks. The ordinals are just a hint used to help indicate extents that correspond to the same start and end blocks.
    startBlock (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Index of the first block that this extent provides.
    endBlock (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Index of the last block that this extent provides.
    reason (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Reason as to why the partition is marked as copy of a VMFS volume's extent. Possible reasons are the disk id is not matching with what the scsi inq is saying or disk uuid is not matchingSee `HostUnresolvedVmfsExtentUnresolvedReason <vim/host/UnresolvedVmfsExtent/UnresolvedReason.rst>`_ 
