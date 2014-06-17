.. _vim.fault.DeviceBackingNotSupported: ../../vim/fault/DeviceBackingNotSupported.rst

.. _VmConfigIncompatibleForFaultTolerance: ../../vim/fault/VmConfigIncompatibleForFaultTolerance.rst


vim.fault.VirtualDiskBlocksNotFullyProvisioned
==============================================
    :extends:

        `vim.fault.DeviceBackingNotSupported`_

  The disk blocks of the specified virtual disk have not been fully provisioned on the file system.Typically, this fault is returned as part of a parent fault like `VmConfigIncompatibleForFaultTolerance`_ , indicating that the disk blocks of the virtual disk must be fully provisioned on the file system before fault tolerance can be enabled on the associated virtual machine.

Attributes:




