.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vmodl.RuntimeFault: ../../vmodl/RuntimeFault.rst


vim.fault.FailToLockFaultToleranceVMs
=====================================
    :extends:

        `vmodl.RuntimeFault`_

  Thrown when trying to state lock a Fault Tolerance VM, and the other VM in the same Fault Tolerance pair is already locked.

Attributes:

    vmName (`str`_)

    vm (`str`_)

    alreadyLockedVm (`str`_)




