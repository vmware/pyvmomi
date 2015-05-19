.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.MigrationFault: ../../vim/fault/MigrationFault.rst


vim.fault.MismatchedVMotionNetworkNames
=======================================
    :extends:

        `vim.fault.MigrationFault`_

  The source and destination hosts do not use the same network name for their VMotion interfaces. This is a warning for migrating powered-on virtual machines.

Attributes:

    sourceNetwork (`str`_)

    destNetwork (`str`_)




