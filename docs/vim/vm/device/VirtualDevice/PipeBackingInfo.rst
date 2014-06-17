.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VirtualDevicePipeBackingInfo: ../../../../vim/vm/device/VirtualDevice/PipeBackingInfo.rst

.. _vim.vm.device.VirtualDevice.BackingInfo: ../../../../vim/vm/device/VirtualDevice/BackingInfo.rst


vim.vm.device.VirtualDevice.PipeBackingInfo
===========================================
  The `VirtualDevicePipeBackingInfo`_ data object type defines information for using a named pipe as backing for a device in a virtual machine.
:extends: vim.vm.device.VirtualDevice.BackingInfo_

Attributes:
    pipeName (`str`_):

       Pipe name for the host pipe associated with this backing.
