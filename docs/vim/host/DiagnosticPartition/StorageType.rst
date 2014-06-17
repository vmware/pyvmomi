.. _vim.host.DiagnosticPartition: ../../../vim/host/DiagnosticPartition.rst

.. _vim.host.DiagnosticPartition.StorageType: ../../../vim/host/DiagnosticPartition/StorageType.rst

vim.host.DiagnosticPartition.StorageType
========================================
  Type of partition indicating the type of storage on which the partition resides. If the diagnostic partition is local only, it will only need one slot. If the diagnostic partition is on shared storage, it could be used by multiple hosts. As a result, it will need multiple slots.
  :contained by: `vim.host.DiagnosticPartition`_

  :type: `vim.host.DiagnosticPartition.StorageType`_

  :name: networkAttached

values:
--------

directAttached
   directAttached

networkAttached
   networkAttached
