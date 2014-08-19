
vim.fault.VAppTaskInProgress
============================
    :extends:

        `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_

  A specialized TaskInProgress when an operation is performed on a VM and it is failed due to a vApp-level operation is in progress. For example, while the power-on sequence is executed on a vApp, individual power-on's of child VMs are failed.

Attributes:




