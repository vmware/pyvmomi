
vim.fault.CannotDisconnectHostWithFaultToleranceVm
==================================================
    :extends:

        `vim.fault.VimFault <vim/fault/VimFault.rst>`_

  This fault is thrown when an attempt is made to disconnect a host, which has one or more fault tolerance vms and is not in maintenance mode.

Attributes:

    hostName (`str <https://docs.python.org/2/library/stdtypes.html>`_)




