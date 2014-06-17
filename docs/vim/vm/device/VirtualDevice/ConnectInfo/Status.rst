.. _vim.vm.device.VirtualDevice.ConnectInfo: ../../../../../vim/vm/device/VirtualDevice/ConnectInfo.rst

.. _vim.vm.device.VirtualDevice.ConnectInfo.Status: ../../../../../vim/vm/device/VirtualDevice/ConnectInfo/Status.rst

vim.vm.device.VirtualDevice.ConnectInfo.Status
==============================================
  Specifies the connectable virtual device status.
  :contained by: `vim.vm.device.VirtualDevice.ConnectInfo`_

  :type: `vim.vm.device.VirtualDevice.ConnectInfo.Status`_

  :name: untried

values:
--------

untried
   The device status is unknown, or it has not been requested to connect when the VM is powered on.

ok
   The device is working correctly.

unrecoverableError
   The device cannot be used. For example, attempting to connect to a floppy device that does not exist would result in this status.

recoverableError
   The device has reported a recoverable error. For example, attempting to connect to floppy device that is being used by another virtual machine or some other program would result in this status.
