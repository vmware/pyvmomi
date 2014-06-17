.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.MigrationFault: ../../vim/fault/MigrationFault.rst


vim.fault.MismatchedNetworkPolicies
===================================
    :extends:

        `vim.fault.MigrationFault`_

  The virtual machine network uses different offload or security policies on the destination host than on the source host. This is an error if the virtual machine is currently connected to the network, and a warning otherwise.

Attributes:

    device (`str`_)

    backing (`str`_)

    connected (`bool`_)




