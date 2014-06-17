.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.CpuIncompatible: ../../vim/fault/CpuIncompatible.rst


vim.fault.FaultToleranceCpuIncompatible
=======================================
    :extends:

        `vim.fault.CpuIncompatible`_

  Convenience subclass for calling out some named features among the incompatibilities found in CPUID level 1 register ecx for FT vms.

Attributes:

    model (`bool`_)

    family (`bool`_)

    stepping (`bool`_)




