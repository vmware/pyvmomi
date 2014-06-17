.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.DeviceNotSupported: ../../vim/fault/DeviceNotSupported.rst

.. _VmConfigIncompatibleForFaultTolerance: ../../vim/fault/VmConfigIncompatibleForFaultTolerance.rst


vim.fault.VirtualDiskModeNotSupported
=====================================
    :extends:

        `vim.fault.DeviceNotSupported`_

  The disk mode of the specified virtual disk is not supported.Typically, this fault is returned as part of a parent fault like `VmConfigIncompatibleForFaultTolerance`_ , indicating that the virtual disk's mode needs to be changed before fault tolerance can be enabled on the associated virtual machine.

Attributes:

    mode (`str`_)




