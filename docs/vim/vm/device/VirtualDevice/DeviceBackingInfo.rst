
vim.vm.device.VirtualDevice.DeviceBackingInfo
=============================================
  The `VirtualDeviceDeviceBackingInfo <vim/vm/device/VirtualDevice/DeviceBackingInfo.rst>`_ data object type defines information about a host device or resource that backs a device in a virtual machine.
:extends: vim.vm.device.VirtualDevice.BackingInfo_

Attributes:
    deviceName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the device on the host system.
    useAutoDetect (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether the device should be auto detected instead of directly specified. If this value is set to TRUE, deviceName is ignored.
