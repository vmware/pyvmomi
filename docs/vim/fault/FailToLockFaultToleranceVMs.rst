
vim.fault.FailToLockFaultToleranceVMs
=====================================
    :extends:

        `vmodl.RuntimeFault <vmodl/RuntimeFault.rst>`_

  Thrown when trying to state lock a Fault Tolerance VM, and the other VM in the same Fault Tolerance pair is already locked.

Attributes:

    vmName (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    vm (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    alreadyLockedVm (`str <https://docs.python.org/2/library/stdtypes.html>`_)




