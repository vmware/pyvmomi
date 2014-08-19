
vim.fault.MismatchedVMotionNetworkNames
=======================================
    :extends:

        `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_

  The source and destination hosts do not use the same network name for their VMotion interfaces. This is a warning for migrating powered-on virtual machines.

Attributes:

    sourceNetwork (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    destNetwork (`str <https://docs.python.org/2/library/stdtypes.html>`_)




