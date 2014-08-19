vim.vm.ScheduledHardwareUpgradeInfo.HardwareUpgradeStatus
=========================================================
  Status for last attempt to run scheduled hardware upgrade.
  :contained by: `vim.vm.ScheduledHardwareUpgradeInfo <vim/vm/ScheduledHardwareUpgradeInfo.rst>`_

  :type: `vim.vm.ScheduledHardwareUpgradeInfo.HardwareUpgradeStatus <vim/vm/ScheduledHardwareUpgradeInfo/HardwareUpgradeStatus.rst>`_

  :name: failed

values:
--------

failed
   Upgrade failed. For more information about the failureSee `fault <vim/vm/ScheduledHardwareUpgradeInfo.rst#fault>`_ 

none
   No scheduled upgrade ever happened.

success
   Upgrade succeeded.

pending
   Upgrade is scheduled, but was not run yet.
