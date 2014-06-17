.. _int: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.VirtualHardwareCompatibilityIssue: ../../vim/fault/VirtualHardwareCompatibilityIssue.rst


vim.fault.MemorySizeNotSupportedByDatastore
===========================================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue`_

  The memory amount of the virtual machine is not within the acceptable guest memory bounds supported by the virtual machine's datastore.

Attributes:

    datastore (`str`_)

    memorySizeMB (`int`_)

    maxMemorySizeMB (`int`_)




