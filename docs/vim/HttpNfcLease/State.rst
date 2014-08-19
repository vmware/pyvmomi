vim.HttpNfcLease.State
======================
  List of possible states of a lease.
  :contained by: `vim.HttpNfcLease <vim/HttpNfcLease.rst>`_

  :type: `vim.HttpNfcLease.State <vim/HttpNfcLease/State.rst>`_

  :name: error

values:
--------

ready
   When the lease is ready and disks may be transferred.

error
   When an error has occurred.

done
   When the import/export session is completed, and the lease is no longer held.

initializing
   When the lease is being initialized.
