.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.CpuIncompatible: ../../vim/fault/CpuIncompatible.rst


vim.fault.CpuIncompatible81EDX
==============================
    :extends:

        `vim.fault.CpuIncompatible`_

  Convenience subclass for calling out some named features among the incompatibilities found in CPUID level 0x80000001 register edx.

Attributes:

    nx (`bool`_)

    ffxsr (`bool`_)

    rdtscp (`bool`_)

    lm (`bool`_)

    other (`bool`_)

    otherOnly (`bool`_)




