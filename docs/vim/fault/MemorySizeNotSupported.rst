.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VirtualHardwareCompatibilityIssue: ../../vim/fault/VirtualHardwareCompatibilityIssue.rst


vim.fault.MemorySizeNotSupported
================================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue`_

  The memory amount of the virtual machine is not within the acceptable guest memory bounds supported by the virtual machine's host.

Attributes:

    memorySizeMB (`int`_)

    minMemorySizeMB (`int`_)

    maxMemorySizeMB (`int`_)




