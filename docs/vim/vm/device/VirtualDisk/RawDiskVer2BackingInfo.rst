
vim.vm.device.VirtualDisk.RawDiskVer2BackingInfo
================================================
  This data object type contains information about backing a virtual disk by using a host device, as used by VMware Server.
:extends: vim.vm.device.VirtualDevice.DeviceBackingInfo_

Attributes:
    descriptorFileName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the raw disk descriptor file.
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Disk UUID for the virtual disk, if available.
    changeId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The change ID of the virtual disk for the corresponding snapshot or virtual machine. This can be used to track incremental changes to a virtual disk. See `QueryChangedDiskAreas <vim/VirtualMachine.rst#queryChangedDiskAreas>`_ .
