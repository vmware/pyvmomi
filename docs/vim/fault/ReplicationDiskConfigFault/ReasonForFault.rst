vim.fault.ReplicationDiskConfigFault.ReasonForFault
===================================================
  :contained by: `vim.fault.ReplicationDiskConfigFault <vim/fault/ReplicationDiskConfigFault.rst>`_

  :type: `vim.fault.ReplicationDiskConfigFault.ReasonForFault <vim/fault/ReplicationDiskConfigFault/ReasonForFault.rst>`_

  :name: reconfigureDiskReplicationIdNotAllowed

values:
--------

duplicateDiskReplicationId
   Another disk in the VM has the same replication ID

invalidPersistentFilePath
   Invalid path (string) for the persistent file

diskNotFound
   Could not look up device by key

reconfigureDiskReplicationIdNotAllowed
   Attempting to re-configure the disk's replication ID

invalidDiskReplicationId
   Invalid disk replication ID string

diskTypeNotSupported
   Replication not supported for disk type or backend

invalidDiskKey
   Invalid key value
