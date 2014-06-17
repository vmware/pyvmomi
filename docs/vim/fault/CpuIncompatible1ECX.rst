.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.CpuIncompatible: ../../vim/fault/CpuIncompatible.rst


vim.fault.CpuIncompatible1ECX
=============================
    :extends:

        `vim.fault.CpuIncompatible`_

  Convenience subclass for calling out some named features among the incompatibilities found in CPUID level 1 register ecx.

Attributes:

    sse3 (`bool`_)

    pclmulqdq (`bool`_)

    ssse3 (`bool`_)

    sse41 (`bool`_)

    sse42 (`bool`_)

    aes (`bool`_)

    other (`bool`_)

    otherOnly (`bool`_)




