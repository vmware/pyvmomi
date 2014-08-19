
vim.fault.PowerOnFtSecondaryFailed
==================================
    :extends:

        `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_

  The PowerOnFtSecondaryFailed fault is thrown when the system is unable to power on a Fault Tolerance secondary virtual machine. It includes a list of failures on different hosts.

Attributes:

    vm (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    vmName (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    hostSelectionBy (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    hostErrors (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    rootCause (`str <https://docs.python.org/2/library/stdtypes.html>`_)




