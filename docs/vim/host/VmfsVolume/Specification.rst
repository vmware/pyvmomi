
vim.host.VmfsVolume.Specification
=================================
  This data object type describes the VMware File System (VMFS) creation specification. Once created, these properties for the most part cannot be changed. There are a few exceptions.
:extends: vmodl.DynamicData_

Attributes:
    extent (`vim.host.ScsiDisk.Partition <vim/host/ScsiDisk/Partition.rst>`_):

       Head extent of VMFS. The head extent identifies the VMFS. However, the head extent should not be used to identify the VMFS across host reboots. The actual identifier is specified in "vmhbaI:T:L" format which is not guaranteed to be stable across reboots. Define a volume name that is unique to the host and use it to refer to the VMFS. Alternatively, the immutable UUID of the VMFS can be used after it is created.
    blockSizeMb (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The block size of VMFS in megabytes (MB). Determines the maximum file size. If this optional property is not set, the maximum file size defaults to the maximum file size for the platform.In VMFS2, the valid block sizes 1MB, 2MB, 4MB, 8MB, 16MB, 32MB, 64MB, 128MB, and 256MB. In VMFS3, the valid block sizes are 1MB, 2MB, 4MB, and 8MB. In VMFS5, the only valid block size is 1MB.
    majorVersion (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Major version number of VMFS. This can be changed if the VMFS is upgraded, but this is an irreversible change.
    volumeName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Volume name of VMFS.
