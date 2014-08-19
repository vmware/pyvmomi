
vim.fault.ApplicationQuiesceFault
=================================
    :extends:

        `vim.fault.SnapshotFault <vim/fault/SnapshotFault.rst>`_

  This fault is thrown when creating a quiesced snapshot failed because the (user-supplied) custom pre-freeze script in the virtual machine exited with a non-zero return code.This indicates that the script failed to perform its quiescing task, which causes us to fail the quiesced snapshot operation.

Attributes:




