.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst


vim.fault.SwapDatastoreUnset
============================
    :extends:

        `vim.fault.VimFault`_

  The compute resource and/or virtual machine configurations indicate that when executing on the host the virtual machine should use a swap datastore, but the host does not have a swap datastore configured. If executing on the host the virtual machine would instead use its own directory for swapfile placement. This is a compatibility warning, not an error. Note it is actually the common case for a host to not have a configured swap datastore, and the problem may rest with the compute resource and/or virtual machine configuration; therefore this is not a HostConfigFault.

Attributes:




