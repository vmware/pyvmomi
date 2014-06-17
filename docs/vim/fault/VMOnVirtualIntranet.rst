.. _vim.fault.CannotAccessNetwork: ../../vim/fault/CannotAccessNetwork.rst


vim.fault.VMOnVirtualIntranet
=============================
    :extends:

        `vim.fault.CannotAccessNetwork`_

  The virtual machine is using a "virtual intranet", a virtual network that exists only within a single host. If returned as part of a migration check, this is an error if the virtual machine is currently connected to the network and a warning otherwise.

Attributes:




