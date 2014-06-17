.. _string: ../../str

.. _vim.fault.VmFaultToleranceIssue: ../../vim/fault/VmFaultToleranceIssue.rst


vim.fault.FaultTolerancePrimaryPowerOnNotAttempted
==================================================
    :extends:

        `vim.fault.VmFaultToleranceIssue`_

  This fault is used to report that VirtualCenter did not attempt to power on a Fault Tolerance secondary virtual machine because it was unable to power on the corresponding Fault Tolerance primary virtual machine.

Attributes:

    secondaryVm (`str`_)

    primaryVm (`str`_)




