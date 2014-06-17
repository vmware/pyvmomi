.. _vim.host.ScsiLun: ../../../vim/host/ScsiLun.rst

.. _vim.host.ScsiLun.State: ../../../vim/host/ScsiLun/State.rst

vim.host.ScsiLun.State
======================
  The Operational state of the LUN
  :contained by: `vim.host.ScsiLun`_

  :type: `vim.host.ScsiLun.State`_

  :name: timeout

values:
--------

quiesced
   The LUN is inactive.

ok
   The LUN is on and available.

unknownState
   The LUN state is unknown.

lostCommunication
   No more paths are available to the LUN.

timeout
   All Paths have been down for the timeout condition determined by a user-configurable host advanced option.

error
   The LUN is dead and/or not reachable.

off
   The LUN is off.

degraded
   One or more paths to the LUN are down, but I/O is still possible. Further path failures may result in lost connectivity.
