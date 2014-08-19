
vim.fault.PowerOnFtSecondaryTimedout
====================================
    :extends:

        `vim.fault.Timedout <vim/fault/Timedout.rst>`_

  PowerOnFtSecondaryTimedout exception is thrown when Virtual Center fails the operation to power on a Fault Tolerance secondary virtual machine because it is taking longer than expected.

Attributes:

    vm (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    vmName (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    timeout (`int <https://docs.python.org/2/library/stdtypes.html>`_)




