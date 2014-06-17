.. _vim.fault.InsufficientResourcesFault: ../../vim/fault/InsufficientResourcesFault.rst


vim.fault.InvalidResourcePoolStructureFault
===========================================
    :extends:

        `vim.fault.InsufficientResourcesFault`_

  This fault is thrown when an operation will cause the structure of a resource pool hiearchy to exceed its limit. The limits are typically imposed by the total number of nodes, maximum fan-out, and total depth of the hierarchy.

Attributes:




