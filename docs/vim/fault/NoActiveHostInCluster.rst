.. _string: ../../str

.. _vim.fault.InvalidState: ../../vim/fault/InvalidState.rst


vim.fault.NoActiveHostInCluster
===============================
    :extends:

        `vim.fault.InvalidState`_

  A NoActiveHostInCluster fault is thrown when there is no host in a valid state in the given compute resource to perform a specified operation. This can happen, for example, if all the hosts are disconnected or in maintenance mode.

Attributes:

    computeResource (`str`_)




