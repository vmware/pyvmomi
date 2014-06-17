.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.MigrationFault: ../../vim/fault/MigrationFault.rst


vim.fault.NetworksMayNotBeTheSame
=================================
    :extends:

        `vim.fault.MigrationFault`_

  Used as a warning if a virtual machine provisioning operation is done across datacenters. This warns that the network used by the virtual machine before and after the operation may not be the same even though the two networks have the same name. This is because network names are only unique within a datacenter.

Attributes:

    name (`str`_): is optional.




