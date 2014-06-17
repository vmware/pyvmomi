.. _vim.Datastore.Summary: ../../../vim/Datastore/Summary.rst

.. _vim.Datastore.Summary.MaintenanceModeState: ../../../vim/Datastore/Summary/MaintenanceModeState.rst

vim.Datastore.Summary.MaintenanceModeState
==========================================
  Defines the current maintenance mode state of the datastore.
  :contained by: `vim.Datastore.Summary`_

  :type: `vim.Datastore.Summary.MaintenanceModeState`_

  :name: inMaintenance

values:
--------

inMaintenance
   Successfully entered maintenance mode.

enteringMaintenance
   Started entering maintenance mode, but not finished. This could happen when waiting for user input or for long-running vmotions to complete.

normal
   Default state.
