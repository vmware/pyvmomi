
vim.fault.VmFaultToleranceTooManyVMsOnHost
==========================================
    :extends:

        `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_

  This fault is returned when a host has more than the recommended number of Fault Tolerance VMs running on it.

Attributes:

    hostName (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    maxNumFtVms (`int <https://docs.python.org/2/library/stdtypes.html>`_)




