.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VirtualHardwareCompatibilityIssue: ../../vim/fault/VirtualHardwareCompatibilityIssue.rst


vim.fault.NumVirtualCoresPerSocketNotSupported
==============================================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue`_

  The host's software does not support enough cores per socket to accomodate the virtual machine. This is always an error.

Attributes:

    maxSupportedCoresPerSocketDest (`int`_)

    numCoresPerSocketVm (`int`_)




