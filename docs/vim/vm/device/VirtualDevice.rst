
vim.vm.device.VirtualDevice
===========================
  VirtualDevice is the base data object type for devices in a virtual machine. This type contains enough information about a virtual device to allow clients to display devices they do not recognize. For example, a client with an older version than the server to which it connects may see a device without knowing what it is.
:extends: vmodl.DynamicData_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       A unique key that distinguishes this device from other devices in the same virtual machine. Keys are immutable but may be recycled; that is, a key does not change as long as the device is associated with a particular virtual machine. However, once a device is removed, its key may be used when another device is added.This property is not read-only, but the client cannot control its value. Persistent device keys are always assigned and managed by the server, which guarantees that all devices will have non-negative key values.When adding new devices, it may be necessary for a client to assign keys temporarily in order to associate controllers with devices in configuring a virtual machine. However, the server does not allow a client to reassign a device key, and the server may assign a different value from the one passed during configuration. Clients should ensure that existing device keys are not reused as temporary key values for the new device to be added (for example, by using unique negative integers as temporary keys).When editing or deleting a device, clients must use the server-provided key to refer to an existing device.
    deviceInfo (`vim.Description <vim/Description.rst>`_, optional):

       Provides a label and summary information for the device.
    backing (`vim.vm.device.VirtualDevice.BackingInfo <vim/vm/device/VirtualDevice/BackingInfo.rst>`_, optional):

       Information about the backing of this virtual device presented in the context of the virtual machine's environment. Not all devices are required to have backing information.See `VirtualMachineConfigOption <vim/vm/ConfigOption.rst>`_ 
    connectable (`vim.vm.device.VirtualDevice.ConnectInfo <vim/vm/device/VirtualDevice/ConnectInfo.rst>`_, optional):

       Provides information about restrictions on removing this device while a virtual machine is running. If the device is not removable, then this property is null.
    slotInfo (`vim.vm.device.VirtualDevice.BusSlotInfo <vim/vm/device/VirtualDevice/BusSlotInfo.rst>`_, optional):

       Information about the bus slot of a device in a virtual machine.
    controllerKey (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Object key for the controller object for this device. This property contains the key property value of the controller device object.
    unitNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The unit number of this device on its controller. This property is null if the controller property is null (for example, when the device is not attached to a specific controller object).Normally, two devices on the same controller may not be assigned the same unit number. If multiple devices could exist on a controller, then unit number has to be specified to configure respective devices.
