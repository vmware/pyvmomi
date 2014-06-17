.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VmFaultToleranceIssue: ../../vim/fault/VmFaultToleranceIssue.rst


vim.fault.InvalidOperationOnSecondaryVm
=======================================
    :extends:

        `vim.fault.VmFaultToleranceIssue`_

  This fault is thrown when an attempt is made to invoke an operation on a secondary virtual machine that is only supported on the primary virtual machine of the fault tolerant group.

Attributes:

    instanceUuid (`str`_)




