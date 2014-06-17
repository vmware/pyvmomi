.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VirtualHardwareCompatibilityIssue: ../../vim/fault/VirtualHardwareCompatibilityIssue.rst


vim.fault.NumVirtualCpusNotSupported
====================================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue`_

  The host's software does not support enough virtual CPUs to accomodate the virtual machine. This is always an error.

Attributes:

    maxSupportedVcpusDest (`int`_)

    numCpuVm (`int`_)




