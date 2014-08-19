
vim.fault.UnusedVirtualDiskBlocksNotScrubbed
============================================
    :extends:

        `vim.fault.DeviceBackingNotSupported <vim/fault/DeviceBackingNotSupported.rst>`_

  The unused disk blocks of the specified virtual disk have not been scrubbed on the file system.Typically, this fault is returned as part of a parent fault like `VmConfigIncompatibleForFaultTolerance <vim/fault/VmConfigIncompatibleForFaultTolerance.rst>`_ , indicating that the unused blocks of the virtual disk must be zeroed-out on the file system before before fault tolerance can be enabled on the associated virtual machine.

Attributes:




