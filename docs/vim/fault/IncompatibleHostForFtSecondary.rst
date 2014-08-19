
vim.fault.IncompatibleHostForFtSecondary
========================================
    :extends:

        `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_

  The IncompatibleHostForFtSecondary fault is thrown when an invalid host has been specified when calling `CreateSecondaryVM_Task <vim/VirtualMachine.rst#createSecondary>`_ or `EnableSecondaryVM_Task <vim/VirtualMachine.rst#enableSecondary>`_ .

Attributes:

    host (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    error (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




