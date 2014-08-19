vim.vm.GuestInfo.ToolsVersionStatus
===================================
  Current version status of VMware Tools installed in the guest operating system.
  :contained by: `vim.vm.GuestInfo <vim/vm/GuestInfo.rst>`_

  :type: `vim.vm.GuestInfo.ToolsVersionStatus <vim/vm/GuestInfo/ToolsVersionStatus.rst>`_

  :name: guestToolsBlacklisted

values:
--------

guestToolsBlacklisted
   VMware Tools is installed, but the installed version is known to have a grave bug and should be immediately upgraded.

guestToolsUnmanaged
   VMware Tools is installed, but it is not managed by VMWare.

guestToolsNeedUpgrade
   VMware Tools is installed, but the version is not current.

guestToolsSupportedOld
   VMware Tools is installed, supported, but a newer version is available.

guestToolsTooOld
   VMware Tools is installed, but the version is too old.

guestToolsTooNew
   VMware Tools is installed, and the version is known to be too new to work correctly with this virtual machine.

guestToolsNotInstalled
   VMware Tools has never been installed.

guestToolsSupportedNew
   VMware Tools is installed, supported, and newer than the version available on the host.

guestToolsCurrent
   VMware Tools is installed, and the version is current.
