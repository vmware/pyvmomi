.. _state: ../../../../vim/vsan/host/DiskResult.rst#state

.. _error: ../../../../vim/vsan/host/DiskResult.rst#error

.. _vim.vsan.host.DiskResult: ../../../../vim/vsan/host/DiskResult.rst

.. _vim.vsan.host.DiskResult.State: ../../../../vim/vsan/host/DiskResult/State.rst

vim.vsan.host.DiskResult.State
==============================
  Values used for indicating a disk's status for use by the VSAN service.See `state`_ 
  :contained by: `vim.vsan.host.DiskResult`_

  :type: `vim.vsan.host.DiskResult.State`_

  :name: ineligible

values:
--------

eligible
   Disk is considered eligible for use by the VSAN service, but is not currently in use.

ineligible
   Disk is considered ineligible for use by the VSAN service, and is not currently in use.See `error`_ 

inUse
   Disk is currently in use by the VSAN service. A disk may be considered in use by the VSAN service regardless of whether the VSAN service is enabled. As long as a disk is in use by VSAN, it is reserved exclusively for VSAN and may not be used for other purposes.See `error`_ 
