.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst


vim.fault.DisableAdminNotSupported
==================================
    :extends:

        `vim.fault.HostConfigFault`_

  Fault thrown when an attempt is made to move a disk with associated snapshots to a destination host. If such a move were to occur, snapshots associated with the disk would be irrevocably lost. This is always an error.

Attributes:




