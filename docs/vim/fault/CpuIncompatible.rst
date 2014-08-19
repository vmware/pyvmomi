
vim.fault.CpuIncompatible
=========================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue <vim/fault/VirtualHardwareCompatibilityIssue.rst>`_

  The host is not compatible with the CPU feature requirements of the virtual machine, for a particular CPUID register. A subclass of this fault may be used to express the incompatibilities in a more easily understandable format.

Attributes:

    level (`int <https://docs.python.org/2/library/stdtypes.html>`_)

    registerName (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    registerBits (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    desiredBits (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    host (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




