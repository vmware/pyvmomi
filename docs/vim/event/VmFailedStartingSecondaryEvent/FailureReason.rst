vim.event.VmFailedStartingSecondaryEvent.FailureReason
======================================================
  The reason for the failure.
  :contained by: `vim.event.VmFailedStartingSecondaryEvent <vim/event/VmFailedStartingSecondaryEvent.rst>`_

  :type: `vim.event.VmFailedStartingSecondaryEvent.FailureReason <vim/event/VmFailedStartingSecondaryEvent/FailureReason.rst>`_

  :name: migrateFailed

values:
--------

incompatibleHost
   Remote host is incompatible for secondary virtual machine. For instance, the host doesn't have access to the virtual machine's network or datastore.

registerVmFailed
   Registration of the secondary virtual machine on the remote host failed.

migrateFailed
   Migration failed.

loginFailed
   Login to remote host failed.
