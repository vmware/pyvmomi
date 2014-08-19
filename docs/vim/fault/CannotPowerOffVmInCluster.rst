
vim.fault.CannotPowerOffVmInCluster
===================================
    :extends:

        `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_

  This fault is reported when a user attempts to power off or suspend a VM when the HA master agent to which vCenter Server is connected does not manage the VM.

Attributes:

    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    vm (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    vmName (`str <https://docs.python.org/2/library/stdtypes.html>`_)




