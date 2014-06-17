.. _defaultValue: ../../../vim/option/BoolOption.rst#defaultValue

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion4

.. _vim.option.BoolOption: ../../../vim/option/BoolOption.rst

.. _VirtualMachineVMCIDevice: ../../../vim/vm/device/VirtualVMCIDevice.rst

.. _VirtualMachineVMCIDeviceOption: ../../../vim/vm/device/VirtualVMCIDeviceOption.rst

.. _vim.vm.device.VirtualDeviceOption: ../../../vim/vm/device/VirtualDeviceOption.rst


vim.vm.device.VirtualVMCIDeviceOption
=====================================
  The `VirtualMachineVMCIDeviceOption`_ data object contains the options for the virtual VMCI device ( `VirtualMachineVMCIDevice`_ ).
:extends: vim.vm.device.VirtualDeviceOption_
:since: `vSphere API 4.0`_

Attributes:
    allowUnrestrictedCommunication (`vim.option.BoolOption`_):

       Indicates support for VMCI communication and specifies the default operation. If `defaultValue`_ is set to true, the virtual machine can participate in VMCI communication with all other virtual machines on the host. Otherwise, VMCI communication will be restricted to trusted services such as the hypervisor on the host.
