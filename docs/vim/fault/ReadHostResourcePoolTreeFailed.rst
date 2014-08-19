
vim.fault.ReadHostResourcePoolTreeFailed
========================================
    :extends:

        `vim.fault.HostConnectFault <vim/fault/HostConnectFault.rst>`_

  Fault thrown on host connect if we were unable to correctly read the existing tree on the root. This is bad because then we don't know the available resources on the host, and all kinds of admission control will fail. This just allows for more robust error handling - we should be able to read the existing hierarchy under normal conditions.

Attributes:




