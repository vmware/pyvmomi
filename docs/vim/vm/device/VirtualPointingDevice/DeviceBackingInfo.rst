.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VirtualPointingDeviceOption: ../../../../vim/vm/device/VirtualPointingDeviceOption.rst

.. _VirtualPointingDeviceHostChoice: ../../../../vim/vm/device/VirtualPointingDeviceOption/DeviceBackingOption/HostPointingDeviceChoice.rst

.. _vim.vm.device.VirtualDevice.DeviceBackingInfo: ../../../../vim/vm/device/VirtualDevice/DeviceBackingInfo.rst


vim.vm.device.VirtualPointingDevice.DeviceBackingInfo
=====================================================
  The VirtualPointingDevice.DeviceBackingInfo provides information about the physical mouse backing the VirtualPointingDevice data object type.
:extends: vim.vm.device.VirtualDevice.DeviceBackingInfo_

Attributes:
    hostPointingDevice (`str`_):

       This optional property defines the mouse type (two-button, three-button, and so on). The mouse type determines how the user interacts with the host mouse. The valid values are specified in the `VirtualPointingDeviceHostChoice`_ list.Note: The value specified by this property must be one of the supported types listed in the hostPointingDevices.value array in the `VirtualPointingDeviceOption`_ data object type. If this property is not set, then the property defaults to the hostPointingDevices.defaultIndex property in the same data object type.
