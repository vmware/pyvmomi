
vim.vm.GuestInfo.DiskInfo
=========================
  Information about each virtual disk configured in the guest operating system.
:extends: vmodl.DynamicData_

Attributes:
    diskPath (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the virtual disk in the guest operating system. For example: C:\
    capacity (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Total capacity of the disk, in bytes. This is part of the virtual machine configuration.
    freeSpace (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Free space on the disk, in bytes. This is retrieved by VMware Tools.
