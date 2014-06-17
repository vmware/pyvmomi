.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.VirtualHardwareCompatibilityIssue: ../../vim/fault/VirtualHardwareCompatibilityIssue.rst


vim.fault.CpuIncompatible
=========================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue`_

  The host is not compatible with the CPU feature requirements of the virtual machine, for a particular CPUID register. A subclass of this fault may be used to express the incompatibilities in a more easily understandable format.

Attributes:

    level (`int`_)

    registerName (`str`_)

    registerBits (`str`_): is optional.

    desiredBits (`str`_): is optional.

    host (`str`_): is optional.




