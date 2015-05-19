.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.MigrationFault: ../../vim/fault/MigrationFault.rst


vim.fault.TooManyDisksOnLegacyHost
==================================
    :extends:

        `vim.fault.MigrationFault`_

  The VM has too many disks which can cause the VM to take a long time to power-on. This can result in migration taking a long time to complete or to fail due to timeout. This is a problem only for migration of powered-on virtual machines from or to ESX 2.x hosts.

Attributes:

    diskCount (`int`_)

    timeoutDanger (`bool`_)




