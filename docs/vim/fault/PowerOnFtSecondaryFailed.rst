.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.VmFaultToleranceIssue: ../../vim/fault/VmFaultToleranceIssue.rst


vim.fault.PowerOnFtSecondaryFailed
==================================
    :extends:

        `vim.fault.VmFaultToleranceIssue`_

  The PowerOnFtSecondaryFailed fault is thrown when the system is unable to power on a Fault Tolerance secondary virtual machine. It includes a list of failures on different hosts.

Attributes:

    vm (`str`_)

    vmName (`str`_)

    hostSelectionBy (`str`_)

    hostErrors (`str`_): is optional.

    rootCause (`str`_)




