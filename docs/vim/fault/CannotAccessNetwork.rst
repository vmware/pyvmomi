
vim.fault.CannotAccessNetwork
=============================
    :extends:

        `vim.fault.CannotAccessVmDevice <vim/fault/CannotAccessVmDevice.rst>`_

  A network associated with the virtual machine is not accessible. If returned as part of migration checks, this is an error if either of the following is true, a warning otherwise:
   * The virtual ethernet card device backing is a distributed virtual switch, of which the destination host is not a member
   * The virtual ethernet card device backing is a standard network and the the device is connected

Attributes:




