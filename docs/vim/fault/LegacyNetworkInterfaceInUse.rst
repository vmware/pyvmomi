
vim.fault.LegacyNetworkInterfaceInUse
=====================================
    :extends:

        `vim.fault.CannotAccessNetwork <vim/fault/CannotAccessNetwork.rst>`_

  A virtual machine's network connectivity cannot be determined because it uses a legacy network interface. If returned as part of migration checks, this is an error if the virtual machine is currently connected to the legacy interface, and a warning otherwise.

Attributes:




