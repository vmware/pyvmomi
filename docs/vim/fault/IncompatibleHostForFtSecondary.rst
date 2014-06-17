.. _string: ../../str

.. _EnableSecondaryVM_Task: ../../vim/VirtualMachine.rst#enableSecondary

.. _CreateSecondaryVM_Task: ../../vim/VirtualMachine.rst#createSecondary

.. _vim.fault.VmFaultToleranceIssue: ../../vim/fault/VmFaultToleranceIssue.rst


vim.fault.IncompatibleHostForFtSecondary
========================================
    :extends:

        `vim.fault.VmFaultToleranceIssue`_

  The IncompatibleHostForFtSecondary fault is thrown when an invalid host has been specified when calling `CreateSecondaryVM_Task`_ or `EnableSecondaryVM_Task`_ .

Attributes:

    host (`str`_)

    error (`str`_): is optional.




