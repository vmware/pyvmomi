
vim.fault.DisallowedDiskModeChange
==================================
    :extends:

        `vim.fault.InvalidDeviceSpec <vim/fault/InvalidDeviceSpec.rst>`_

  Thrown when the `ReconfigVM_Task <vim/VirtualMachine.rst#reconfigure>`_ operation includes a change to the `VirtualDiskMode <vim/vm/device/VirtualDiskOption/DiskMode.rst>`_ property. This property cannot be changed as long as a virtual machine has an existing snapshot.

Attributes:




