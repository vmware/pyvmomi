vim.LicenseManager.LicenseState
===============================
  State of licensing subsystem.
  :contained by: `vim.LicenseManager <vim/LicenseManager.rst>`_

  :type: `vim.LicenseManager.LicenseState <vim/LicenseManager/LicenseState.rst>`_

  :name: fault

values:
--------

marginal
   License source unavailable, using license cache.

normal
   Running within operating parameters.

fault
   Initialization has failed or grace period expired.

initializing
   Setting or resetting configuration in progress.
