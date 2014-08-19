
vim.fault.DestinationSwitchFull
===============================
    :extends:

        `vim.fault.CannotAccessNetwork <vim/fault/CannotAccessNetwork.rst>`_

  For one of the networks that the virtual machine is using, the corresponding switch on the host is full. If returned as part of migration checks, this is an error if either of the following is true, a warning otherwise:
   * The virtual ethernet card device backing is a distributed virtual switch
   * The virtual ethernet card device backing is a standard network and the the device is connected

Attributes:




