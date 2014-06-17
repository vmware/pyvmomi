.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.MigrationFault: ../../vim/fault/MigrationFault.rst


vim.fault.ReadOnlyDisksWithLegacyDestination
============================================
    :extends:

        `vim.fault.MigrationFault`_

  The virtual machine uses read-only (undoable or nonpersistent) disks that can cause a slower power on at the migration destination. As a result, VMtion could slow down considerably or timeout. This is an issue only for migration of powered-on virtual machines from an ESX host with version greater than 2.0.x to an ESX host with version 2.0.x. It will be an error if the number of such disks is great enough to cause timeout ( >= 3 ), or a warning otherwise.

Attributes:

    roDiskCount (`int`_)

    timeoutDanger (`bool`_)




