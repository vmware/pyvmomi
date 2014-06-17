.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.vm.device.VirtualDevice: ../../vim/vm/device/VirtualDevice.rst


vim.vm.VirtualHardware
======================
  The VirtualHardware data object type contains the complete configuration of the hardware in a virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    numCPU (`int`_):

       Number of virtual CPUs present in this virtual machine.
    numCoresPerSocket (`int`_, optional):

       Number of cores used to distribute virtual CPUs among sockets in this virtual machine. If the value is unset it implies to numCoresPerSocket = 1.
    memoryMB (`int`_):

       Memory size, in MB.
    virtualICH7MPresent (`bool`_, optional):

       Does this virtual machine have Virtual Intel I/O Controller Hub 7
    virtualSMCPresent (`bool`_, optional):

       Does this virtual machine have System Management Controller
    device (`vim.vm.device.VirtualDevice`_, optional):

       The set of virtual devices belonging to the virtual machine. This list is unordered.
