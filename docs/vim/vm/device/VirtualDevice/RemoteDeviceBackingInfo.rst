.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VirtualDeviceRemoteDeviceBackingInfo: ../../../../vim/vm/device/VirtualDevice/RemoteDeviceBackingInfo.rst

.. _vim.vm.device.VirtualDevice.BackingInfo: ../../../../vim/vm/device/VirtualDevice/BackingInfo.rst


vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo
===================================================
   `VirtualDeviceRemoteDeviceBackingInfo`_ is a data object type for information about a remote device backing used by a device in a virtual machine. The primary difference between a remote device backing and a local device backing is that the VirtualCenter server cannot provide a list of remote host devices available for this virtual device backing.
:extends: vim.vm.device.VirtualDevice.BackingInfo_

Attributes:
    deviceName (`str`_):

       The name of the device on the remote system.
    useAutoDetect (`bool`_, optional):

       Indicates whether the device should be auto detected instead of directly specified. If this value is set to TRUE,deviceNameis ignored.
