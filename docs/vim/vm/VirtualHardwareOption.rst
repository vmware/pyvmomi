
vim.vm.VirtualHardwareOption
============================
  The VirtualHardwareOption data object contains the options available for all virtual devices.
:extends: vmodl.DynamicData_

Attributes:
    hwVersion (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The virtual hardware version.
    virtualDeviceOption ([`vim.vm.device.VirtualDeviceOption <vim/vm/device/VirtualDeviceOption.rst>`_]):

       Array of virtual device options valid for this virtual machine configuration. The list is unordered.
    deviceListReadonly (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether the set of virtual devices can be changed, e.g., can devices be added or removed. This does not preclude changing devices.
    numCPU ([`int <https://docs.python.org/2/library/stdtypes.html>`_]):

       List of acceptable values for the number of CPUs supported by this `ConfigOption <vim/vm/ConfigOption.rst>`_ . This is usually superceded by the information available in the guest operating system descriptors. The guest operating system descriptor describes a maximum CPU count, but the acceptable values are still constrained to the set specified here. The default value is stored at index 0 in the list.
    numCoresPerSocket (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum and default number of cores per socket that can be used when distributing virtual CPUs.
    numCpuReadonly (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Can the number of virtual CPUs be changed
    memoryMB (`vim.option.LongOption <vim/option/LongOption.rst>`_):

       The minimum, maximum, and default memory options, in MB, per virtual machine, for this VirtualHardwareOption. These values are typically overruled by the supported and recommended values specified in the `GuestOsDescriptor <vim/vm/GuestOsDescriptor.rst>`_ class.
    numPCIControllers (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum, and default number of PCI controllers for this virtual machine configuration.
    numIDEControllers (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum, and default number of IDE controllers for this virtual machine configuration. Note: SCSI controllers sit on the PCI controller so their options (minimum, maximum, and default values) are contained inside the `VirtualPCIControllerOption <vim/vm/device/VirtualPCIControllerOption.rst>`_ class.
    numUSBControllers (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum, and default number of USB controllers for this virtual machine configuration.
    numUSBXHCIControllers (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum, and default number of XHCI (USB 3.0) controllers for this virtual machine configuration.
    numSIOControllers (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum, and default number of SIO controllers for this virtual machine configuration.
    numPS2Controllers (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum, and default number of PS2 controllers for this virtual machine configuration.
    licensingLimit ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of propery names which limits are given be a licensing restriction of the underlying product, e.g., a limit that is not derived based on the product or hardware features. For example, the property name "numCPU"
    numSupportedWwnPorts (`vim.option.IntOption <vim/option/IntOption.rst>`_, optional):

       The minimum, maximum and default number of NPIV WorldWideNode names supported for this virtual machine configuration.
    numSupportedWwnNodes (`vim.option.IntOption <vim/option/IntOption.rst>`_, optional):

       The minimum, maximum and default number of NPIV WorldWidePort names supported for this virtual machine configuration.
    resourceConfigOption (`vim.ResourceConfigOption <vim/ResourceConfigOption.rst>`_):

       Default value and value range for `ResourceConfigOption <vim/ResourceConfigOption.rst>`_ 
