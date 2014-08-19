
vim.fault.FaultToleranceCpuIncompatible
=======================================
    :extends:

        `vim.fault.CpuIncompatible <vim/fault/CpuIncompatible.rst>`_

  Convenience subclass for calling out some named features among the incompatibilities found in CPUID level 1 register ecx for FT vms.

Attributes:

    model (`bool <https://docs.python.org/2/library/stdtypes.html>`_)

    family (`bool <https://docs.python.org/2/library/stdtypes.html>`_)

    stepping (`bool <https://docs.python.org/2/library/stdtypes.html>`_)




