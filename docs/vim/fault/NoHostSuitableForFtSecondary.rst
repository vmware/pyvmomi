
vim.fault.NoHostSuitableForFtSecondary
======================================
    :extends:

        `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_

  The NoHostSuitableForFtSecondary fault is thrown when the system is unable to find a suitable host for the Fault Tolerance secondary virtual machine. This fault can be thrown when Virtual Center is trying to place or power on a Fault Tolerance Secondary, in both DRS or non-DRS cases.

Attributes:

    vm (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    vmName (`str <https://docs.python.org/2/library/stdtypes.html>`_)




