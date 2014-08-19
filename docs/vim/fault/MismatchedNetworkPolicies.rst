
vim.fault.MismatchedNetworkPolicies
===================================
    :extends:

        `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_

  The virtual machine network uses different offload or security policies on the destination host than on the source host. This is an error if the virtual machine is currently connected to the network, and a warning otherwise.

Attributes:

    device (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    backing (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    connected (`bool <https://docs.python.org/2/library/stdtypes.html>`_)




