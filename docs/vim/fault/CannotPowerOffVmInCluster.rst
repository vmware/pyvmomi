.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.InvalidState: ../../vim/fault/InvalidState.rst


vim.fault.CannotPowerOffVmInCluster
===================================
    :extends:

        `vim.fault.InvalidState`_

  This fault is reported when a user attempts to power off or suspend a VM when the HA master agent to which vCenter Server is connected does not manage the VM.

Attributes:

    operation (`str`_)

    vm (`str`_)

    vmName (`str`_)




