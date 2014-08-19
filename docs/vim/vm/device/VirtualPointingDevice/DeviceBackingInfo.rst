
vim.vm.device.VirtualPointingDevice.DeviceBackingInfo
=====================================================
  The VirtualPointingDevice.DeviceBackingInfo provides information about the physical mouse backing the VirtualPointingDevice data object type.
:extends: vim.vm.device.VirtualDevice.DeviceBackingInfo_

Attributes:
    hostPointingDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       This optional property defines the mouse type (two-button, three-button, and so on). The mouse type determines how the user interacts with the host mouse. The valid values are specified in the `VirtualPointingDeviceHostChoice <vim/vm/device/VirtualPointingDeviceOption/DeviceBackingOption/HostPointingDeviceChoice.rst>`_ list.Note: The value specified by this property must be one of the supported types listed in the hostPointingDevices.value array in the `VirtualPointingDeviceOption <vim/vm/device/VirtualPointingDeviceOption.rst>`_ data object type. If this property is not set, then the property defaults to the hostPointingDevices.defaultIndex property in the same data object type.
