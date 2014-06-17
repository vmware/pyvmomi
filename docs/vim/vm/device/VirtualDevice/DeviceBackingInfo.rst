.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VirtualDeviceDeviceBackingInfo: ../../../../vim/vm/device/VirtualDevice/DeviceBackingInfo.rst

.. _vim.vm.device.VirtualDevice.BackingInfo: ../../../../vim/vm/device/VirtualDevice/BackingInfo.rst


vim.vm.device.VirtualDevice.DeviceBackingInfo
=============================================
  The `VirtualDeviceDeviceBackingInfo`_ data object type defines information about a host device or resource that backs a device in a virtual machine.
:extends: vim.vm.device.VirtualDevice.BackingInfo_

Attributes:
    deviceName (`str`_):

       The name of the device on the host system.
    useAutoDetect (`bool`_, optional):

       Indicates whether the device should be auto detected instead of directly specified. If this value is set to TRUE, deviceName is ignored.
