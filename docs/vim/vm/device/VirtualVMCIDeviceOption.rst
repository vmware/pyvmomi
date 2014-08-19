
vim.vm.device.VirtualVMCIDeviceOption
=====================================
  The `VirtualMachineVMCIDeviceOption <vim/vm/device/VirtualVMCIDeviceOption.rst>`_ data object contains the options for the virtual VMCI device ( `VirtualMachineVMCIDevice <vim/vm/device/VirtualVMCIDevice.rst>`_ ).
:extends: vim.vm.device.VirtualDeviceOption_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion4>`_

Attributes:
    allowUnrestrictedCommunication (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Indicates support for VMCI communication and specifies the default operation. If `defaultValue <vim/option/BoolOption.rst#defaultValue>`_ is set to true, the virtual machine can participate in VMCI communication with all other virtual machines on the host. Otherwise, VMCI communication will be restricted to trusted services such as the hypervisor on the host.
