.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.InvalidFolder: ../../vim/fault/InvalidFolder.rst


vim.fault.VmAlreadyExistsInDatacenter
=====================================
    :extends:

        `vim.fault.InvalidFolder`_

  Fault thrown when moving a standalone host between datacenters, and one or more of the virtual machines registered on the host are already registered to hosts in the target datacenter.

Attributes:

    host (`str`_)

    hostname (`str`_)

    vm (`str`_)




