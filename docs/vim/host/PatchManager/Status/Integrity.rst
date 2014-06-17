.. _vim.host.PatchManager.Status: ../../../../vim/host/PatchManager/Status.rst

.. _vim.host.PatchManager.Status.Integrity: ../../../../vim/host/PatchManager/Status/Integrity.rst

vim.host.PatchManager.Status.Integrity
======================================
  The integrity validation status.
  :contained by: `vim.host.PatchManager.Status`_

  :type: `vim.host.PatchManager.Status.Integrity`_

  :name: validationError

values:
--------

validated
   The update is successfully validated.

validationError
   The integrity validation failed.

digestMismatch
   A digital signature of the update does not match.

notEnoughSignatures
   Not enough signed signatures on the update.

keyExpired
   A public key to verify the update is expired.

keyNotFound
   The integrity can not be verified since a public key to verify the update cannot be found.

keyRevoked
   A public key to verify the update has been revoked.
