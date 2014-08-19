
vim.vm.check.Result
===================
  The result of a call to any of the methods in either `VirtualMachineCompatibilityChecker <vim/vm/check/CompatibilityChecker.rst>`_ or `VirtualMachineProvisioningChecker <vim/vm/check/ProvisioningChecker.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_, optional):

       The virtual machine involved in the testing.
    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):

       The host involved in the testing.
    warning ([`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_], optional):

       A list of faults representing problems which may require attention, but which are not fatal.
    error ([`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_], optional):

       A list of faults representing problems which are fatal to the operation. For `VirtualMachineProvisioningChecker <vim/vm/check/ProvisioningChecker.rst>`_ an error means that the given provisioning operation would fail. For `VirtualMachineCompatibilityChecker <vim/vm/check/CompatibilityChecker.rst>`_ an error means that either a power-on of this virtual machine would fail, or that the virtual machine would not run correctly once powered-on.
