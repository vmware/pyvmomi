.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst


vim.fault.ConcurrentAccess
==========================
    :extends:

        `vim.fault.VimFault`_

  A ConcurrentAccess fault is thrown when an operation fails because another operation has modified the datastructure.For non-transactional operations, such as a recursive delete of a subtree of the inventory, the operation might fail with ConcurrentAccess if another thread has added a new entity to the hierarchy.

Attributes:




