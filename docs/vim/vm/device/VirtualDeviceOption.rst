
vim.vm.device.VirtualDeviceOption
=================================
  The VirtualDeviceOption data object type contains information about a virtual device type, the options for configuring the virtual device, and the relationship between this virtual device and other devices. The vSphere API groups device configurations that are mutually exclusive into different configuration objects; each of these configuration objects may define subtypes for virtual device backing options that are independent of the virtual device. Backing-dependent options should appear in a subtype of `VirtualDeviceBackingOption <vim/vm/device/VirtualDeviceOption/BackingOption.rst>`_ .
:extends: vmodl.DynamicData_

Attributes:
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the run-time class the client should instantiate to create a run-time instance of this device.
    connectOption (`vim.vm.device.VirtualDeviceOption.ConnectOption <vim/vm/device/VirtualDeviceOption/ConnectOption.rst>`_, optional):

       If the device is connectable, then the connectOption describes the connect options and defaults.
    busSlotOption (`vim.vm.device.VirtualDeviceOption.BusSlotOption <vim/vm/device/VirtualDeviceOption/BusSlotOption.rst>`_, optional):

       If the device can use a bus slot configuration, then the busSlotOption describes the bus slot options.
    controllerType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Data object type that denotes the controller option object that is valid for controlling this device.
    autoAssignController (`vim.option.BoolOption <vim/option/BoolOption.rst>`_, optional):

       Flag to indicate whether or not this device will be auto-assigned a controller if one is required. If this is true, then a client need not explicitly create the controller that this device will plug into.
    backingOption ([`vim.vm.device.VirtualDeviceOption.BackingOption <vim/vm/device/VirtualDeviceOption/BackingOption.rst>`_], optional):

       A list of backing options that can be used to map the virtual device to the host. The list is optional, since some devices exist only within the virtual machine; for example, a VirtualController.
    defaultBackingOptionIndex (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Index into the backingOption list, indicating the default backing.
    licensingLimit ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of property names enforced by a licensing restriction of the underlying product. For example, a limit that is not derived based on the product or hardware features; the property name "numCPU".
    deprecated (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether this device is deprecated. Hence, if set the device cannot be used when creating a new virtual machine or be added to an existing virtual machine. However, the device is still supported by the platform.
    plugAndPlay (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates if this type of device can be hot-added to the virtual machine via a reconfigure operation when the virtual machine is powered on.
    hotRemoveSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates if this type of device can be hot-removed from the virtual machine via a reconfigure operation when the virtual machine is powered on.
