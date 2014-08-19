
vim.host.PciDevice
==================
  This data object type describes information about a single Peripheral Component Interconnect (PCI) device.
:extends: vmodl.DynamicData_

Attributes:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name ID of this PCI, composed of "bus:slot.function".
    classId (`short <https://docs.python.org/2/library/stdtypes.html>`_):

       The class of this PCI.
    bus (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The bus ID of this PCI.
    slot (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The slot ID of this PCI.
    function (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The function ID of this PCI.
    vendorId (`short <https://docs.python.org/2/library/stdtypes.html>`_):

       The vendor ID of this PCI.The vendor ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI vendor ID. The WSDL representation of the ID is a signed short integer. If the vendor ID is greater than 32767, the Server will convert the ID to its two's complement for the WSDL representation. When you specify a PCI device vendor ID for a virtual machine ( `VirtualPCIPassthroughDeviceBackingInfo <vim/vm/device/VirtualPCIPassthrough/DeviceBackingInfo.rst>`_ .vendorId), you must use the retrieved `HostPciDevice <vim/host/PciDevice.rst>`_ .deviceId value.
    subVendorId (`short <https://docs.python.org/2/library/stdtypes.html>`_):

       The subvendor ID of this PCI.The subvendor ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI subvendor ID. The WSDL representation of the ID is a signed short integer. If the subvendor ID is greater than 32767, the Server will convert the ID to its two's complement for the WSDL representation.
    vendorName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The vendor name of this PCI.
    deviceId (`short <https://docs.python.org/2/library/stdtypes.html>`_):

       The device ID of this PCI.The device ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI device ID. The WSDL representation of the ID is a signed short integer. If the PCI ID is greater than 32767, the Server will convert the ID to its two's complement for the WSDL representation. When you specify a PCI device ID for a virtual machine ( `VirtualPCIPassthroughDeviceBackingInfo <vim/vm/device/VirtualPCIPassthrough/DeviceBackingInfo.rst>`_ .deviceId), you must use the `HostPciDevice <vim/host/PciDevice.rst>`_ .deviceId value as retrieved and convert it to a string.
    subDeviceId (`short <https://docs.python.org/2/library/stdtypes.html>`_):

       The subdevice ID of this PCI.The subdevice ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI subdevice ID. The WSDL representation of the ID is a signed short integer. If the subdevice ID is greater than 32767, the Server will convert the ID to its two's complement for the WSDL representation.
    parentBridge (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The parent bridge of this PCI.
    deviceName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The device name of this PCI.
