
vim.host.DatastoreBrowser.VmDiskInfo
====================================
  This data object type describes a virtual disk primary file.
:extends: vim.host.DatastoreBrowser.FileInfo_

Attributes:
    diskType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Disk type of the virtual disk.The specified disk type is one of the backing information types for a virtual disk.See `VirtualDisk <vim/vm/device/VirtualDisk.rst>`_ 
    capacityKb (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The capacity of a virtual disk from the point of view of a virtual machine.
    hardwareVersion (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The hardware version of the virtual disk file.
    controllerType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The controller type suitable for this virtual disk.
    diskExtents ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The extents of this virtual disk specified in absolute DS paths
    thin (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates if the disk is thin-provisioned
