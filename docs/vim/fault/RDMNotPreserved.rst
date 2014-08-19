
vim.fault.RDMNotPreserved
=========================
    :extends:

        `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_

  The virtual machine is configured with a Raw Disk Mapping. The host only supports Raw Disk Mappings in a limited fashion. After the migration, the RDM will function correctly, but it will be indistinguishable from a virtual disk when viewing the virtual machine's properties. This change will persist even if the virtual machine is migrated back to a host with full RDM support.This is a warning only for migrations to ESX 2.1.x hosts.

Attributes:

    device (`str <https://docs.python.org/2/library/stdtypes.html>`_)




