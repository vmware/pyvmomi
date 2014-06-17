.. _str: https://docs.python.org/2/library/stdtypes.html

.. _short: https://docs.python.org/2/library/stdtypes.html

.. _HostPciDevice: ../../../../vim/host/PciDevice.rst

.. _vSphere API 4.0: ../../../../vim/version.rst#vimversionversion5

.. _vim.vm.device.VirtualDevice.DeviceBackingInfo: ../../../../vim/vm/device/VirtualDevice/DeviceBackingInfo.rst


vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo
=====================================================
  The VirtualPCIPassthrough.DeviceBackingInfo data object type contains information about the backing that maps the virtual device onto a physical device.
:extends: vim.vm.device.VirtualDevice.DeviceBackingInfo_
:since: `vSphere API 4.0`_

Attributes:
    id (`str`_):

       The name ID of this PCI, composed of "bus:slot.function".
    deviceId (`str`_):

       The device ID of this PCI. You must use the device ID retrieved from the vSphere host ( `HostPciDevice`_ .deviceId), converted as is to a string.
    systemId (`str`_):

       The ID of the system the PCI device is attached to.
    vendorId (`short`_):

       The vendor ID for this PCI device. You must use the vendor ID retrieved from the vSphere host ( `HostPciDevice`_ .vendorId).
