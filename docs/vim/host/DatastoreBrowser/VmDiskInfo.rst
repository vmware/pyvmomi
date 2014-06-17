.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VirtualDisk: ../../../vim/vm/device/VirtualDisk.rst

.. _vim.host.DatastoreBrowser.FileInfo: ../../../vim/host/DatastoreBrowser/FileInfo.rst


vim.host.DatastoreBrowser.VmDiskInfo
====================================
  This data object type describes a virtual disk primary file.
:extends: vim.host.DatastoreBrowser.FileInfo_

Attributes:
    diskType (`str`_, optional):

       Disk type of the virtual disk.The specified disk type is one of the backing information types for a virtual disk.See `VirtualDisk`_ 
    capacityKb (`long`_, optional):

       The capacity of a virtual disk from the point of view of a virtual machine.
    hardwareVersion (`int`_, optional):

       The hardware version of the virtual disk file.
    controllerType (`str`_, optional):

       The controller type suitable for this virtual disk.
    diskExtents (`str`_, optional):

       The extents of this virtual disk specified in absolute DS paths
    thin (`bool`_, optional):

       Indicates if the disk is thin-provisioned
