.. _vim.host.PatchManager.Status: ../../../../vim/host/PatchManager/Status.rst

.. _vim.host.PatchManager.Status.Reason: ../../../../vim/host/PatchManager/Status/Reason.rst

vim.host.PatchManager.Status.Reason
===================================
  Reasons why an update is not applicable to the ESX host.
  :contained by: `vim.host.PatchManager.Status`_

  :type: `vim.host.PatchManager.Status.Reason`_

  :name: conflictLib

values:
--------

conflictLib
   The update conflicts with RPMs or libraries installed on the host.

obsoleted
   The update is made obsolete by other patches installed on the host.

hasDependentPatch
   The update depends on an update that is not installed but is in the scanned list of updates.

missingPatch
   The update depends on another update that is neither installed nor in the scanned list of updates.

missingLib
   The update depends on certain libraries or RPMs that are not available.

conflictPatch
   The update conflicts with certain updates that are already installed on the host.
