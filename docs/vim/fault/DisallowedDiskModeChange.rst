.. _VirtualDiskMode: ../../vim/vm/device/VirtualDiskOption/DiskMode.rst

.. _ReconfigVM_Task: ../../vim/VirtualMachine.rst#reconfigure

.. _vim.fault.InvalidDeviceSpec: ../../vim/fault/InvalidDeviceSpec.rst


vim.fault.DisallowedDiskModeChange
==================================
    :extends:

        `vim.fault.InvalidDeviceSpec`_

  Thrown when the `ReconfigVM_Task`_ operation includes a change to the `VirtualDiskMode`_ property. This property cannot be changed as long as a virtual machine has an existing snapshot.

Attributes:




