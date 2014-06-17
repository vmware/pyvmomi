.. _vim.fault.SnapshotFault: ../../vim/fault/SnapshotFault.rst


vim.fault.SnapshotNoChange
==========================
    :extends:

        `vim.fault.SnapshotFault`_

  This fault is for a snapshot request on a virtual machine whose state has not changed since a previous successful snapshot. For example, this occurs when you suspend the virtual machine, create a snapshot, and then request another snapshot of the suspended virtual machine.

Attributes:




