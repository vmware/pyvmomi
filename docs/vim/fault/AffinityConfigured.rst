.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.MigrationFault: ../../vim/fault/MigrationFault.rst


vim.fault.AffinityConfigured
============================
    :extends:

        `vim.fault.MigrationFault`_

  Virtual machine has a configured memory and/or CPU affinity that will prevent VMotion. This is an error for powered-on virtual machines.

Attributes:

    configuredAffinity (`str`_)




