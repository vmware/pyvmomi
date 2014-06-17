.. _vim.vm.device.VirtualDeviceSpec: ../../../../vim/vm/device/VirtualDeviceSpec.rst

.. _vim.vm.device.VirtualDeviceSpec.FileOperation: ../../../../vim/vm/device/VirtualDeviceSpec/FileOperation.rst

vim.vm.device.VirtualDeviceSpec.FileOperation
=============================================
  The type of operation being performed on the backing of a virtual device. Valid values are:
  :contained by: `vim.vm.device.VirtualDeviceSpec`_

  :type: `vim.vm.device.VirtualDeviceSpec.FileOperation`_

  :name: replace

values:
--------

destroy
   Specifies the destruction of a device backing.

create
   Specifies the creation of the device backing; for example, the creation of a virtual disk or floppy image file.

replace
   Specifies the deletion of the existing backing for a virtual device and the creation of a new backing.
