
vim.fault.SwapDatastoreNotWritableOnHost
========================================
    :extends:

        `vim.fault.DatastoreNotWritableOnHost <vim/fault/DatastoreNotWritableOnHost.rst>`_

  The compute resource and/or virtual machine configurations indicate that when executing on the host the virtual machine should use a specific datastore, but host does not have read/write access to that datastore. (It may have no access at all, or read-only access.) If executing on the host the virtual machine would instead use its own directory for swapfile placement. This is a compatibility warning, not an error.

Attributes:




