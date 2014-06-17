.. _vim.vm.GuestInfo: ../../../vim/vm/GuestInfo.rst

.. _vim.vm.GuestInfo.ToolsStatus: ../../../vim/vm/GuestInfo/ToolsStatus.rst

vim.vm.GuestInfo.ToolsStatus
============================
  Current status of VMware Tools running in the guest operating system.
  :contained by: `vim.vm.GuestInfo`_

  :type: `vim.vm.GuestInfo.ToolsStatus`_

  :name: toolsOk

values:
--------

toolsOk
   VMware Tools is running and the version is current.

toolsNotInstalled
   VMware Tools has never been installed or has not run in the virtual machine.

toolsOld
   VMware Tools is running, but the version is not current.

toolsNotRunning
   VMware Tools is not running.
