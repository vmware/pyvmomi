
vim.fault.NumVirtualCpusExceedsLimit
====================================
    :extends:

        `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_

  This fault is thrown when the total number of virtual CPUs present or requested in virtual machines' configuration has exceeded the limit on the host.

Attributes:

    maxSupportedVcpus (`int <https://docs.python.org/2/library/stdtypes.html>`_)




