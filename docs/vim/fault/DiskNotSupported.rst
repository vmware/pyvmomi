.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VirtualHardwareCompatibilityIssue: ../../vim/fault/VirtualHardwareCompatibilityIssue.rst


vim.fault.DiskNotSupported
==========================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue`_

  The host does not support the backings for the disks specified by the virtual machine. For example, this fault is thrown if a virtual machine is created from a template that specifies backings that the host does not have. Similarly, this fault is thrown if a virtual machine is registered on a host that does not support the specified backings.

Attributes:

    disk (`int`_)




