.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VirtualHardwareCompatibilityIssue: ../../vim/fault/VirtualHardwareCompatibilityIssue.rst


vim.fault.NotEnoughCpus
=======================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue`_

  The host hardware does not have enough CPU cores to support the number of virtual CPUs in the virtual machine.If the host is using hyperthreading, NotEnoughLogicalCpus is employed instead of NotEnoughCpus.

Attributes:

    numCpuDest (`int`_)

    numCpuVm (`int`_)




