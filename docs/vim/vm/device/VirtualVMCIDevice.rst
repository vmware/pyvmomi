
vim.vm.device.VirtualVMCIDevice
===============================
  The `VirtualMachineVMCIDevice <vim/vm/device/VirtualVMCIDevice.rst>`_ data object represents a virtual communication device that supports the VMCI (Virtual Machine Communication Interface). Each virtual machine has a VMCI device that handles interprocess socket-based communication. VMCI device information is available in the virtual machine hardware device list ( `VirtualMachine <vim/VirtualMachine.rst>`_ . `config <vim/VirtualMachine.rst#config>`_ . `hardware <vim/vm/ConfigInfo.rst#hardware>`_ . `device <vim/vm/VirtualHardware.rst#device>`_ []).An application running on a virtual machine uses the VMCI Sockets API for communication with other virtual machines on the same host (communication between virtual machines is not supported on vSphere 5.1 and later platforms as described for VirtualVMCIDevice. `allowUnrestrictedCommunication <vim/vm/device/VirtualVMCIDevice.rst#allowUnrestrictedCommunication>`_ ), or for communication with the host. For information about using the vSphere VMCI Sockets API, see theVMCI Sockets Programming Guide.
:extends: vim.vm.device.VirtualDevice_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion4>`_

Attributes:
    id (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Unique identifier for VMCI socket access to this virtual machine. Use this value to identify this virtual machine in calls to the VMCI Sockets API. Applications running on other virtual machines on this host will use this value to connect to this virtual machine. You can cast this value to a 32-bit unsigned integer.The vSphere Server sets this value when a virtual machine powers on. The Server may change this value after power operations such as vMotion or restoring a virtual machine from a snapshot. If you have saved a VMCI device identifier, check to see if the value is still valid after power operations.
    allowUnrestrictedCommunication (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Determines the extent of VMCI communication with this virtual machine. Set this property to true to allow VMCI communication with all virtual machines on the host and with trusted services. Set this property to false to allow VMCI communication only with trusted services such as the hypervisor on the host.If unset, communication is restricted to trusted services only.
