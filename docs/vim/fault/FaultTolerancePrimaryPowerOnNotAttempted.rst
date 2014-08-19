
vim.fault.FaultTolerancePrimaryPowerOnNotAttempted
==================================================
    :extends:

        `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_

  This fault is used to report that VirtualCenter did not attempt to power on a Fault Tolerance secondary virtual machine because it was unable to power on the corresponding Fault Tolerance primary virtual machine.

Attributes:

    secondaryVm (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    primaryVm (`str <https://docs.python.org/2/library/stdtypes.html>`_)




