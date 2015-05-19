.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../../vim/VirtualMachine.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst

.. _VirtualMachineProvisioningChecker: ../../../vim/vm/check/ProvisioningChecker.rst

.. _VirtualMachineCompatibilityChecker: ../../../vim/vm/check/CompatibilityChecker.rst


vim.vm.check.Result
===================
  The result of a call to any of the methods in either `VirtualMachineCompatibilityChecker`_ or `VirtualMachineProvisioningChecker`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    vm (`vim.VirtualMachine`_, optional):

       The virtual machine involved in the testing.
    host (`vim.HostSystem`_, optional):

       The host involved in the testing.
    warning ([`vmodl.LocalizedMethodFault`_], optional):

       A list of faults representing problems which may require attention, but which are not fatal.
    error ([`vmodl.LocalizedMethodFault`_], optional):

       A list of faults representing problems which are fatal to the operation. For `VirtualMachineProvisioningChecker`_ an error means that the given provisioning operation would fail. For `VirtualMachineCompatibilityChecker`_ an error means that either a power-on of this virtual machine would fail, or that the virtual machine would not run correctly once powered-on.
